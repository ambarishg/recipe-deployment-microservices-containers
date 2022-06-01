# Install the Azure Container Apps extension for the CLI.
az extension add --name containerapp --upgrade

# Now that the extension is installed, register the Microsoft.App namespace.
az provider register --namespace Microsoft.App

# Register the Microsoft.OperationalInsights provider for the Azure Monitor Log Analytics Workspace if you have not used it before.
az provider register --namespace Microsoft.OperationalInsights       

RESOURCE_GROUP="winegroup"         
LOCATION="canadacentral"                 
CONTAINERAPPS_ENVIRONMENT="redwine-env"  

# Create a Resource Group           
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create an Environment
az containerapp env create --name $CONTAINERAPPS_ENVIRONMENT --resource-group $RESOURCE_GROUP --location $LOCATION

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

# Create the Container App           
az containerapp create \
--name redwineapp \
--resource-group $RESOURCE_GROUP \
--environment $CONTAINERAPPS_ENVIRONMENT \
--image agwineacr.azurecr.io/redwineflask:v1  \
--registry-server agwineacr.azurecr.io \
--registry-username agwineacr \
--registry-password $password  \
--target-port 5000 \
--ingress 'external' \
--query configuration.ingress.fqdn
