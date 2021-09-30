This repo will show 
* How to break a monolithic into a microservice               
* How to deploy a microservice in local Docker Desktop           
* How to deploy a microservice in local Kubernetes Cluster                
* How to deploy a microservice in Azure Container Instances          
* How to deploy a microservice in Azure Kubernetes Cluster               
* How to deploy a microservice in AWS Fargate          
* How to deploy a microservice in AWS EKS                   

# Folders    

* **redwine-streamlit-monolithic** has the UI as well as the code with it. This is a monolithic application        

* **redwine-streamlit-server** is a microservice implementation with the microservice implemented in Python using Flask framework. The functions are       
    * predict - which uses a deep learning model to predict the quality of redwine    
    * hello - test function to test the deployment is done correctly          

* **redwine-client** is a console based application which calls the the microservice implemented in **redwine-streamlit-server**           

* **redwine-client** is a console based application which calls the the microservice implemented in **redwine-streamlit-server**    

* **redwine-streamlit** is a Streamlit based application which calls the the microservice implemented in **redwine-streamlit-server**    

# **redwine-streamlit-server**

|  FileName  |  Description |
|---|---|
| app.py |   Has the microservice implementation        |
|  Dockerfile | Docker file for the microservice to produce a container image   |
|  requirements.txt | The libraries required for the Dockerfile are present in the requirements.txt. The Dockerfile uses the requirements.txt   |
|  docker-steps.md | The steps required to deploy the microservices container in the local Docker Desktop and the local Docker Kubernetes cluster  |
|  redwine-local.yaml | The YAML file which we would be using in the local Kubernetes cluster  |
