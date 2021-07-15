plant-pathology-2021

docker build -t gcr.io/${PROJECT_ID}/hello-app:v1 .

docker tag ambarishg/redwine:v1 gcr.io/plant-pathology-2021/redwine-repo:v1

gcloud services enable containerregistry.googleapis.com

gcloud auth configure-docker

docker push gcr.io/plant-pathology-2021/redwine-repo:v1

############################################################

gcloud config set project plant-pathology-2021   

gcloud config set compute/zone COMPUTE_ZONE
gcloud config set compute/zone us-west1-a

gcloud services enable container.googleapis.com

gcloud container clusters create redwine-cluster --num-nodes=1
kubectl get nodes

############################################################

gcloud container clusters get-credentials redwine-cluster --zone us-west1-a  

kubectl create deployment redwine-app --image=gcr.io/plant-pathology-2021/redwine-repo:v1

kubectl expose deployment redwine-app --name=redwine-app-service --type=LoadBalancer --port 8501 --target-port 8501  

kubectl get service

############################################################
kubectl delete service redwine-app-service 
gcloud container clusters delete redwine-cluster --zone us-west1-a  
gcloud container images delete gcr.io/plant-pathology-2021/redwine:v1  --force-delete-tags --quiet

############################################################

kubectl apply -f redwine-gcp.yaml
kubectl delete deploy windedeploy
kubectl delete service redwine-service
gcloud container clusters delete redwine-cluster --zone us-west1-a  
gcloud container images delete gcr.io/plant-pathology-2021/redwine:v1  --force-delete-tags --quiet
############################################################