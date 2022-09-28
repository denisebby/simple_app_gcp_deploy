# What I want to learn:

- how to store models (big and small, nn's, trees, linear, etc.)
    - where do we store them? (within gcp? huggging face?)
- how to store data (gcs?)
- how to set up billing/ budgets/ so as to not incur large cost
- how to interact with an api

# Future goals
- oauth
- payments (stripe?)

# Resources

https://www.youtube.com/watch?v=fw6NMQrYc6w (Daniel Bourke, deploying image classification model to GCP)
- he trained a model with colab
- he saved model to gcs on colab (but this can be done with google cloud sdk)
- AI Platform
    - host model on AI Platform, can create versions of models on AI platform
    - AI platform looks for stored model in gcs bucket
    - online prediction deployment, can configure autoscaling (will scale down when there is less demand)
    - has a hard limit of 1.5 MB
- create service account (to access model)
    - grant the right access (he used ML Engine Developer)
    - create private key from the service account, can specify key type (JSON or P12)
- gcloud app deploy app.yaml
- build docker file
- upload to GCR

## Tips to save money
(how to save money with app engine, set budget)
https://stackoverflow.com/questions/47125661/pricing-of-google-app-engine-flexible-env-a-500-lesson

- we can programaticallly disable cloud billing on a project
- set a cap on API usage

Note to self; I had to set up an organization in order to get all the necessary permissions to make everything work for automatically disabling cloud billing.

publish test message to disable billing
https://github.com/aioverlords/Google-Cloud-Platform-Killswitch/blob/main/pub-sub-sample-message
{
    "budgetDisplayName": "name-of-budget",
    "alertThresholdExceeded": 1.0,
    "costAmount": 100.01,
    "costIntervalStart": "2019-01-01T00:00:00Z",
    "budgetAmount": 100.00,
    "budgetAmountType": "SPECIFIED_AMOUNT",
    "currencyCode": "USD"
}

worst case scenario: can manually disable billing for the project in gcp 

### limiting API usage

### app engine standard vs flex env
https://cloud.google.com/appengine/docs/the-appengine-environments#comparing_high-level_features
use standard to run for free or at very low cost

## Comparison of hosting options
https://dev.to/pcraig3/cloud-run-vs-app-engine-a-head-to-head-comparison-using-facts-and-science-1225

compare google cloud run vs google app engine vs heroku

https://www.techtarget.com/searchcloudcomputing/tip/Compare-Google-Cloud-Run-vs-App-Engine-for-enterprise-software

cloud run won't work for applications that require a persistent file system

# cloud run
https://www.youtube.com/watch?v=1VewIO2Yhmo






