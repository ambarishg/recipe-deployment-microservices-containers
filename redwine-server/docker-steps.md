# Build the docker image   ( Run in Console )       
docker build -t redwineflask .   

# Run Docker   ( Run in Console )    
docker run -p 5000:5000 redwineflask

<!-- docker exec -it <container name> /bin/bash  -->
docker exec -it  confident_moore /bin/bash 

<!-- kubectl config use-context my-cluster-name   -->
kubectl config use-context docker-desktop

docker tag  redwineflask:latest ambarishg/redwineflask:v1
docker push  ambarishg/redwineflask:v1

kubectl apply -f redwine-local.yaml


