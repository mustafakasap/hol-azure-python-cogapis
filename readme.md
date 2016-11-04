# Microsoft Cognitive Services APIs with Python

Microsoft Cognitive Services (formerly Project Oxford) are a set of APIs, SDKs and services available to developers to make their applications more intelligent, engaging and discoverable. [Here you can find a **Jupyter Notebook**](./cognitive_apis.ipynb) with test code for each Cognitive servive APIs.  

**List of services available:**

- Search
    - Bing Autosuggest API
    - Bing Image Search API
    - Bing News Search API
    - Bing Video Search API
    - Bing Web Search API
    
- Vision
    - Computer Vision API
    - Emotion API
    - Face API
    - Video API
    
- Speech
    - Bing Speech API
    - Custom Recognition Intelligent Service (CRIS)
    - Speaker Recognition API
    
- Language
    - Bing Spell Check API
    - Language Understanding Intelligent Service (LUIS)
    - Linguistic Analysis API
    - Text Analytics API ([Click for sample project on **Topic Detection**](./textanalytics_topic.md))
    - Web Language Model API
    
- Knowledge
    - Academic Knowledge API
    - Entity Linking Intelligent Service
    - Knowledge Exploration Service
    - Recommendations API

## Signing-up Cognitive Services APIs:
You can sign-up for any of the above services from [request trial](https://www.microsoft.com/cognitive-services/en-us/subscriptions) page, or from your Azure Management Portal with following steps.

1. Go to the Azure Portal at http://portal.azure.com/ and sign in with your Azure account.

2. Click on + New.

3. Select the Intelligence option.

4. Select the Cognitive Services APIs product. This product will allow you to start a subscription for any of the cognitive services APIs (Face, Text Analytics, Computer Vision, etc.).

5. On the Cognitive Services API landing page, enter the Account name for your service subscription. (For instace: "MyFaceRecService, MyRecommendations"). This name should not have any spaces in it.

6. On API type, select one of the services (Face, Text Analytics, Computer Vision, etc.) that you want to subscribe.

7. On Pricing tier, you can select a plan. You may select the Free tier i.e. for 10,000 transactions/month. This is a free plan, so it is a good way to start trying the system. Once you go to production, we recommend you consider your request volume and change the plan type accordingly. (Note: You can have only one Free tier subscription at a time)

8. Select a Resource Group, or create a new one if you don't have one already.

9. You may change other elements in the Create dialog. We should point out that the resource provider today is only supported from United States data centers.

10. Once you are done with any selections, click Create.

11. Wait a few minutes for the resource to be deployed. Once it is deployed, you can go to the Keys section in the Settings blade where you will be provided a primary and secondary key to use the API. Copy the primary key, as you'll need it when creating your first model.