


## to build image locally
template: docker build -t gcr.io/project_id/python-image:tag

docker build -t gcr.io/united-impact-363519/simple_app:v1.0.0 .

docker buildx build --platform linux/amd64 -t gcr.io/united-impact-363519/simple_app:v1.0.0 .

(use docker build to rebuild image as well)

https://www.youtube.com/watch?v=CSb-sHNM2NY
(can build a yaml file and  use docker compose to actively test with changed images)

## to push to gcs from local
docker push gcr.io/united-impact-363519/simple_app:v1.0.0

## run locally

docker run --platform linux/amd64 -d -p 8080:8080 --name simple-app-container gcr.io/united-impact-363519/simple_app:v1.0.0

## stop container
docker stop

# Skip building image locally
gcloud builds submit --tag gcr.io/ProjectID/simple_app  --project=ProjectID