kubectl config use-context docker-desktop
docker tag redwineflask:latest ambarishg/redwineflask:v1 
docker push ambarishg/redwineflask:v1    

kubectl apply -f redwine-local.yaml

docker tag ambarishg/redwineflask:v1 agwineacr.azurecr.io/redwine:v1 
docker tag ambarishg/redwineflask:v1 redwine:v1 

docker run -p <host port>:<container port> ambarishg/redwine:v1
docker run -p 5000:5000 redwineflask:latest 
<!-- docker run -p 8501:8501 ambarishg/redwine:v1
docker run -p 8555:8501 ambarishg/redwine:v1
docker run -p 8501:8501 agwineacr.azurecr.io/redwine:v1  -->


docker exec -it <container name> /bin/bash 
docker exec -it  winedeploy-d49fc7649-bf78n /bin/bash 


