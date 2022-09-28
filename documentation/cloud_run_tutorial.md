https://www.youtube.com/watch?v=_XAk5T_4-O0

gcloud builds submit --tag gcr.io/ProjectID/dash-youtube-example  --project=ProjectID

gcloud run deploy --image gcr.io/united-impact-363519/simple_app:v1.0.0 --platform managed  --project=united-impact-363519 --allow-unauthenticated

# debug

ERROR: (gcloud.run.deploy) The user-provided container failed to start and listen on the port defined provided by the PORT=8080 environment variable. Logs for this revision might contain more information.

solved by: 
