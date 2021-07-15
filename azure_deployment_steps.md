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

# Push image  
docker push agwineacr.azurecr.io/redwine:v1

# Update the  Azure Container Registry 
az acr update -n agwineacr --admin-enabled true       

# Get the password of the Azure CLI 
password=$(az acr credential show --name agwineacr --query passwords[0].value --output tsv)

# Create the Azure Container    
az container create  --resource-group winegroup  \
--name redwine --image agwineacr.azurecr.io/redwine:v1  \
--registry-login-server agwineacr.azurecr.io \
--ip-address Public  --location centralindia  \
--registry-username agwineacr \
--registry-password $password  \
--ports 8501 --dns-name-label redwineapp   

# Navigate to http://redwineapp.centralindia.azurecontainer.io:8501/

# Cleanup ( Run in Console)   
az group delete --resource-group winegroup


