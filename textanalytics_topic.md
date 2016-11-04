# Cognitive Services - Text Analytics API
This [**sample python project**](./mstextanalytics.py) is developed as text analytics and topic detection showcase demo. For getting better performance over this technology, you should provide a large corpus as an input. In this sample we will show how to use [Text Analytics API](https://www.microsoft.com/cognitive-services/en-us/text-analytics-api) under [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services/en-us/apis) to detect topics inside a corpus. We will develop Python code to access REST APIs of the service. As an example, we will analyse the 2016 presidential debate's transcript. Transcripts can directly be accessed from its sources on Internet provided below. For simplicity, we parse the transcript with very basic operations to split into sentences. Reason for split operation is that the API requires at least 100 chunks of input (each will have at least 3 words) from the corpus to be analyzed. i.e. 100 chapters from a book or 100 subsections of a chapter etc. So we split the whole speech of a speaker into sentences to achieve this criteria. Sentences are determined according to "." fullstop which is not always the case (i.e. some sentences end with question mark or some sentences are divided into pieces because of row width etc.) There are better ways (i.e. using nltk etc.) to split them in meaningful pieces for better result. 

**2016 US Presidential Debate's Transcripts**  
[Final debate source](http://www.politico.com/story/2016/10/full-transcript-third-2016-presidential-debate-230063): http://www.politico.com/story/2016/10/full-transcript-third-2016-presidential-debate-230063  
[Second debate source](http://www.politico.com/story/2016/10/2016-presidential-debate-transcript-229519): http://www.politico.com/story/2016/10/2016-presidential-debate-transcript-229519  
[First debate source](http://www.politico.com/story/2016/10/2016-presidential-debate-transcript-229519): http://www.politico.com/story/2016/10/2016-presidential-debate-transcript-229519

You may need to update the code when analysing transcripts from different sources as the structure may differ.

To run the sample, you need a subscription to Text Analytics API. There is an option for free tier (low performance, limited) subscription for these services.

#### Sign-up Text Analytics APIs:
You can sign-up for any of the above services from [request trial](https://www.microsoft.com/cognitive-services/en-us/subscriptions) page, or from your Azure Management Portal with following steps.

1. Go to the Azure Portal at http://portal.azure.com/ and sign in with your Azure account.

2. Click on + New.

3. Select the Intelligence option.

4. Select the Cognitive Services APIs product. This product will allow you to start a subscription for any of the cognitive services APIs (Face, Text Analytics, Computer Vision, etc.).

5. On the Cognitive Services API landing page, enter the Account name for your service subscription. (For instace: "MyFaceRecService, MyRecommendations"). This name should not have any spaces in it.

6. On API type, select one of the services (Face, **Text Analytics**, Computer Vision, etc.) that you want to subscribe.

7. On Pricing tier, you can select a plan. You may select the Free tier i.e. for 10,000 transactions/month. This is a free plan, so it is a good way to start trying the system. Once you go to production, we recommend you consider your request volume and change the plan type accordingly. (Note: You can have only one Free tier subscription at a time)

8. Select a Resource Group, or create a new one if you don't have one already.

9. You may change other elements in the Create dialog. We should point out that the resource provider today is only supported from United States data centers.

10. Once you are done with any selections, click Create.

11. Wait a few seconds for the resource to be deployed. Once it is deployed, you can go to the Keys section in the Settings blade where you will be provided a **primary and secondary key to use the API**. Copy the primary key, as you'll need it when creating your first model.

#### Running the code & Output
Running the code, you will get the results in *few minutes*. Before you run the code, you should update the *api_key* variable on top of the code with your own key. Above section mentioned how to get that key. The one in the code is expired sample key which will not work for you. Details of the compute intensive parts etc. are commented inside the code, so you may want to put some additional status messages to track which section of the code is running.

Key Phrases with score < 2 are not listed:

#### Final Debate's Results:  
----------------- Analytics for Clinton -----------------  

| Key Phrase              | Score |
| ---                     | --- |
| Donald                  | 13.0 |
| families                | 7.0 |
| gun                     | 6.0 |
| Americans               | 5.0 |
| decisions               | 5.0 |
| court                   | 5.0 |
| President Obama         | 5.0 |
| Trump                   | 4.0 |
| businesses              | 4.0 |
| program                 | 3.0 |
| time                    | 3.0 |
| force                   | 3.0 |
| children                | 3.0 |
| Supreme Court           | 3.0 |
| espionage               | 3.0 |
| attacks                 | 3.0 |
| nuclear weapons         | 3.0 |
| intelligence            | 3.0 |
| tax cuts                | 3.0 |
| undocumented workers    | 2.0 |
| undocumented immigrants | 2.0 |
| Clinton Foundation      | 2.0 |
| Chinese steel           | 2.0 |
| border security         | 2.0 |
| Citizens United         | 2.0 |
| fly zone                | 2.0 |
| Russian government      | 2.0 |
| penny                   | 2.0 |
| Bush administration     | 2.0 |

----------------- Analytics for Trump -----------------  

| Key Phrase              | Score |  
| ---                     | --- | 
| country                 | 22.0 |
| Hillary                 | 9.0 |
| disaster                | 9.0 |
| deal                    | 7.0 |
| taxes                   | 6.0 |
| laws                    | 6.0 |
| Putin                   | 6.0 |
| Russia                  | 6.0 |
| justices                | 6.0 |
| plan                    | 5.0 |
| United                  | 5.0 |
| amendment               | 5.0 |
| NAFTA                   | 5.0 |
| women                   | 4.0 |
| jobs                    | 4.0 |
| campaign                | 4.0 |
| money                   | 4.0 |
| Obama                   | 4.0 |
| Syria                   | 4.0 |
| wall                    | 4.0 |
| pro-life                | 4.0 |
| Chris                   | 3.0 |
| reports                 | 3.0 |
| step                    | 3.0 |
| ISIS                    | 3.0 |
| Court                   | 3.0 |
| NATO                    | 3.0 |
| husband                 | 3.0 |
| fiction                 | 3.0 |
| border                  | 2.0 |
| citizen                 | 2.0 |
| leaders                 | 2.0 |
| Mosul                   | 2.0 |
| job                     | 2.0 |
| cease                   | 2.0 |
| week                    | 2.0 |
| Hillary Clinton         | 2.0 |
| law                     | 2.0 |
| worst deals             | 2.0 |
| trade deals             | 2.0 |
| business                | 2.0 |
| jail                    | 2.0 |
| presidency              | 2.0 |
| FBI                     | 2.0 |
| times                   | 2.0 |
| fame                    | 2.0 |
| rallies                 | 2.0 |
| stories                 | 2.0 |
| violence                | 2.0 |
| Foundation              | 2.0 |


#### Second Debate's Results:  

----------------- Analytics for Clinton -----------------  

| Key Phrase         | Score |  
| ---                | --- | 
| Donald             | 19.0 |
| tax                | 8.0 |
| president          | 7.0 |
| Americans          | 6.0 |
| health insurance   | 5.0 |
| Donald Trump       | 4.0 |
| Muslims            | 4.0 |
| America            | 4.0 |
| incomes            | 4.0 |
| ground             | 4.0 |
| Syria              | 4.0 |
| Care               | 3.0 |
| question           | 3.0 |
| Supreme Court      | 2.0 |
| president Lincoln  | 2.0 |
| President Obama    | 2.0 |
| Middle East        | 2.0 |
| force              | 2.0 |
| women              | 2.0 |

----------------- Analytics for Trump -----------------  

| Key Phrase         | Score |  
| ---                | --- | 
| Hillary Clinton    | 10.0 |
| Obama              | 10.0 |
| ISIS               | 7.0 |
| President Obama    | 5.0 |
| energy             | 4.0 |
| judgment           | 4.0 |
| women              | 3.0 |
| companies          | 3.0 |
| provisions         | 3.0 |
| Hillary            | 3.0 |
| tax code           | 3.0 |
| health care        | 3.0 |
| deal               | 3.0 |
| deficit            | 3.0 |
| businesses         | 3.0 |
| energy companies   | 2.0 |
| respect for women  | 2.0 |
| bad judgment       | 2.0 |
| steel              | 2.0 |
| balance sheet      | 2.0 |
| Abraham Lincoln    | 2.0 |

#### First Debate's Results:  

----------------- Analytics for Clinton -----------------  

| Key Phrase         | Score |  
| ---                | --- | 
| Donald             | 19.0 |
| tax                | 8.0 |
| president          | 7.0 |
| Americans          | 6.0 |
| health insurance   | 5.0 |
| Donald Trump       | 4.0 |
| Muslims            | 4.0 |
| America            | 4.0 |
| incomes            | 4.0 |
| ground             | 4.0 |
| Syria              | 4.0 |
| Care               | 3.0 |
| question           | 3.0 |
| Supreme Court      | 2.0 |
| president Lincoln  | 2.0 |
| President Obama    | 2.0 |
| Middle East        | 2.0 |
| force              | 2.0 |
| women              | 2.0 |

----------------- Analytics for Trump -----------------  

| Key Phrase         | Score |  
| ---                | --- | 
| Hillary Clinton    | 10.0 |
| Obama              | 10.0 |
| ISIS               | 7.0 |
| President Obama    | 5.0 |
| energy             | 4.0 |
| judgment           | 4.0 |
| women              | 3.0 |
| companies          | 3.0 |
| provisions         | 3.0 |
| Hillary            | 3.0 |
| tax code           | 3.0 |
| health care        | 3.0 |
| deal               | 3.0 |
| deficit            | 3.0 |
| businesses         | 3.0 |
| energy companies   | 2.0 |
| respect for women  | 2.0 |
| bad judgment       | 2.0 |
| steel              | 2.0 |
| balance sheet      | 2.0 |
| Abraham Lincoln    | 2.0 |