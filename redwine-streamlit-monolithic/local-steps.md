docker tag redwine:latest ambarishg/redwine:v1 

docker push ambarishg/redwine:v1    

kubectl apply -f redwine-local.yaml

docker tag ambarishg/redwine:v1 agwineacr.azurecr.io/redwine:v1 
docker tag ambarishg/redwine:v1 redwine:v1 

docker run -p <host port>:<container port> ambarishg/redwine:v1
docker run -p 8501:8501 ambarishg/redwine:v1
docker run -p 8555:8501 ambarishg/redwine:v1
docker run -p 8501:8501 agwineacr.azurecr.io/redwine:v1 
docker run -p 8501:8501 redwine:v1 

docker exec -it <container name> /bin/bash 
docker exec -it  busy_lederberg /bin/bash 

