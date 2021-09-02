# get the current default subscription using show
az account show --output table

# Create a Resource Group    ( Run in Console )       
az group create --location centralindia --resource-group winegroup 

# Create a Azure Container Registry   ( Run in Console )   
az acr create --resource-group winegroup --name agwineacr --sku Basic 

# Login into the Azure Container Registry ( Run in Console)     
az acr login -n agwineacr   

# Tag image ( Run in Console)      

docker tag redwineflask:latest agwineacr.azurecr.io/redwineflask:v1   

# Push image ( Run in Console)    
docker push agwineacr.azurecr.io/redwineflask:v1

# Update the  Azure Container Registry ( Run in Console) 
az acr update -n agwineacr --admin-enabled true       

# Get the password of the Azure CLI ( Run in Azure CLI )   
password=$(az acr credential show --name agwineacr --query passwords[0].value --output tsv)

# Create the Azure Container ( Run in Azure CLI )        
az container create  --resource-group winegroup  \
--name redwine --image agwineacr.azurecr.io/redwineflask:v1  \
--registry-login-server agwineacr.azurecr.io \
--ip-address Public  --location centralindia  \
--registry-username agwineacr \
--registry-password $password  \
--ports 5000 --dns-name-label redwineapp   

# Navigate to http://redwineapp.centralindia.azurecontainer.io:5000/

# Cleanup ( Run in Console)   
az group delete --resource-group winegroup




