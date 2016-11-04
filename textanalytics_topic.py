import urllib.request # for html content download, Internet access
from lxml import html # for html parsing, xpath access
import re # for regular expression
import requests # For Rest API call
import json # parse json response
import time # for sleeping in rest api call status checks

# Global variables that will be used in various places in the code.
# Dont forget to update the api-key with your own key. To get your own key, read the readme.md file in this repo
url_text_api = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/topics' # service address 
api_key = '25fdf6b1e4854750aa6f3bdcfba2d8af'          # Azure Cognitive API Key, replace with your own key

# GET page content that contains Trump, Clinton debate transcript
# You can chang the URL with first and second debates urls.
url = 'http://www.politico.com/story/2016/10/full-transcript-third-2016-presidential-debate-230063'
html_response = urllib.request.urlopen(url)
html_content = html_response.read()

# parse page content to get per speaker's talk. This parse technique specific to the above website. 
# It assumes that the speaker speech starts with following html tag format:
#       <p><b>Clinton</b>: There is a lot of evidence about the very good work -- </p>
#       <p><b>SPEAKER</b>: ..... </p>
tree = html.fromstring(html_content)
clinton_turns = tree.xpath('//p[b=\'Clinton\']/text()')
trump_turns = tree.xpath('//p[b=\'Trump\']/text()')

# Text Analytics API requires min 100 document. Each speakers turn may be less then 100 so 
# raughly split each turn into sentences (very basic split approach used...) where number of sentences will be > 100 
# assuming in a single debate, each speaker used more than 100 sentence. Than dividing number of sentence to 100 to find
# how many sentence in each bucket of 100 document requirement
# you can use better sentence extraction etc. i.e. nltk library

# initial empty lists. will be filled with each speaker sentences
clinton_sentences = []
trump_sentences = []

# parse each speakers turn (sentences that are used in his/her turn) into a list
# so further filtering may applied
def generate_sentence_list(speaker_turns, sentence_list):
    for turn in speaker_turns:
        filtered = turn[2:]
        filtered = filtered.replace('(Laughter)', '')
        filtered = filtered.replace('\'', '’')
        filtered = filtered.replace('\n', ' ')
        filtered = filtered.replace('\r', ' ')
        filtered = filtered.replace('\"', '`')
        # you can use https://regex101.com/ to see what this regular expression does.
        sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', filtered)                
        sentence_list.extend(sentences)

# Now each speakers sentences are in the list (as said, need better parsin but this will still work)
generate_sentence_list(clinton_turns, clinton_sentences)
generate_sentence_list(trump_turns, trump_sentences)


# Now we will call Microsoft Text Analytics API to detect topics in each speakers whole speech
# More information about general usage of API: https://www.microsoft.com/cognitive-services/en-us/text-analytics-api 
# Detailed usage information about Topic Detection API: https://azure.microsoft.com/en-us/documentation/articles/cognitive-services-text-analytics-quick-start/ 
# We will use REST APIs

# generate body message of the REST API call
def generate_rest_body(sentences):
    # divide sentences into 100 bucket (per speaker)
    sentence_per_bucket = int(len(sentences)/100)

    i = 0
    docid = 0
    docs = ''

    while i < len(sentences) - 1 - sentence_per_bucket:
        doctext = ''
        for j in range(sentence_per_bucket):
            doctext = doctext + ' ' + sentences[i + j]
        
        i = i + sentence_per_bucket
        docid = docid + 1

        docs = docs + ('{"id":"%s", "text":"%s"}, ' % (docid, doctext))
        
    topics = '{"documents": [ %s ] }' % docs

    return topics

# Generate rest api body in json format
# you can use http://jsonviewer.stack.hu/ to parse the body content
clinton_body = generate_rest_body(clinton_sentences)
trump_body = generate_rest_body(trump_sentences)

# Text Analytics API REST call
def text_analytics(msg_body):
    headers = {'Content-Length': '0', 'Ocp-Apim-Subscription-Key':api_key}

    headers = {'Ocp-Apim-Subscription-Key':api_key, \
            'Content-type': 'application/json',\
            'Accept': 'application/json'}

    api_response = requests.post(url_text_api, headers=headers, data=msg_body.encode('utf-8'))

    return api_response

# Call text analytics API per speaker
# API call will not produce a result immediately. Request will be processed at the backend and when the result is ready, user will be notified.
# To get the process status, user must call the "Operation-Location" parameter returned in the first response header.
clinton_call_result = text_analytics(clinton_body)
trump_call_result = text_analytics(trump_body)

# Get 'Operation-Location'
def get_operation_stat(stat_url): 
    headers = {'Ocp-Apim-Subscription-Key':api_key, \
            'Content-type': 'application/json',\
            'Accept': 'application/json'}

    process_status = requests.get(stat_url, headers=headers)

    return process_status

def get_topics(api_call):
    # status code 202 (not handling all for simplicity) means result is being processed
    # check actual proc status from the url in the header
    if api_call.status_code == 202:
        stat_url = api_call.headers['Operation-Location']

        not_ready = True
        while not_ready:
            proc_stat = get_operation_stat(stat_url)
            res_json = json.loads(proc_stat.content.decode('utf-8'))
            print(res_json['status'])
            if (res_json['status'] != 'Succeeded'):  # other status codes may: NotStarted, Running
                time.sleep(61)
            else:
                not_ready = False

    res_topics = res_json['operationProcessingResult']['topics']
    return res_topics

clinton_topics = get_topics(clinton_call_result)
trump_topics = get_topics(trump_call_result)

cs = sorted(clinton_topics, key=lambda k: k.get('score'), reverse=True)
ts = sorted(trump_topics, key=lambda k: k.get('score'), reverse=True)

print(json.dumps(clinton_topics, indent=2))
print('------------------------')
print(json.dumps(trump_topics, indent=2))
print('------------------------\n\n\n\n')

print('----------------- Analytics for Clinton -----------------')
print('Key Phrase                    Score')
for i in cs:
    print('{0: <30} {1}'.format(i['keyPhrase'], i['score']))
print('\n\n\n\n')
print('----------------- Analytics for Trump -----------------')
print('Key Phrase                    Score')
for i in ts:
    print('{0: <30} {1}'.format(i['keyPhrase'], i['score']))
