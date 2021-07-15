cd /mnt/c/Ambarish/streamlit/redwine

# Build the docker image  with Name and optionally a tag in the 'name:tag' format      
docker build -t redwine .   

# Run Docker   ( Run in Console )    
docker run -p <host port>:<container port> redwine
docker run -p 8501:8501 redwine

# SSH into a container  
docker ps
docker exec -it <container name> /bin/bash
docker exec -it <container name> <command name>
docker exec -it eager_khayyam /bin/bash

# Retag a local image with a new image name and tag 
docker tag redwine:latest  docker.io/ambarishg/redwine:v1

docker push ambarishg/redwine:v1
