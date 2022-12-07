az account show --output table

# Build the docker image       
docker build -t redwine .   

# Run Docker   
docker run -p 8501:8501 redwine

# Create a Resource Group      
az group create --location centralindia --resource-group winegroup 

# Create a Azure Container Registry    
az acr create --resource-group winegroup --name agwineacr --sku Basic 

# Login into the Azure Container Registry   
az acr login -n agwineacr   

# Tag image      
docker tag redwine:latest agwineacr.azurecr.io/redwine:v1  

# Push the image into the Azure Container Registry  
docker push agwineacr.azurecr.io/redwine:v1  


# Create AKS cluster
az aks create \
    --resource-group winegroup \
    --name winecluster \
    --node-count 1 \
    --generate-ssh-keys \
    --attach-acr agwineacr

# Get AKS cluster credentials
az aks get-credentials --resource-group winegroup --name winecluster


# Create pods and service 
kubectl apply -f redwine-azure.yaml

# Cleanup ( Run in Console)   
az group delete --resource-group winegroup