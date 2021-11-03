# Install the Azure Container Apps extension to the CLI.         
az extension add \
  --source https://workerappscliextension.blob.core.windows.net/azure-cli-extension/containerapp-0.2.0-py2.py3-none-any.whl      

# Register the Microsoft.Web namespace       
az provider register --namespace Microsoft.Web          

# Create the Resource group        
RESOURCE_GROUP="winegroup"         
LOCATION="canadacentral"          
LOG_ANALYTICS_WORKSPACE="redwine-logs"          
CONTAINERAPPS_ENVIRONMENT="redwine-env"        

az group create \        
  --name $RESOURCE_GROUP \           
  --location "$LOCATION"       

# Create an environment                
  
az monitor log-analytics workspace create \        
  --resource-group $RESOURCE_GROUP \         
  --workspace-name $LOG_ANALYTICS_WORKSPACE        

LOG_ANALYTICS_WORKSPACE_CLIENT_ID=`az monitor log-analytics workspace show --query customerId -g $RESOURCE_GROUP -n $LOG_ANALYTICS_WORKSPACE --out tsv`             

LOG_ANALYTICS_WORKSPACE_CLIENT_SECRET=`az monitor log-analytics workspace get-shared-keys --query primarySharedKey -g $RESOURCE_GROUP -n $LOG_ANALYTICS_WORKSPACE --out tsv`           

az containerapp env create \
  --name $CONTAINERAPPS_ENVIRONMENT \
  --resource-group $RESOURCE_GROUP \
  --logs-workspace-id $LOG_ANALYTICS_WORKSPACE_CLIENT_ID \
  --logs-workspace-key $LOG_ANALYTICS_WORKSPACE_CLIENT_SECRET \
  --location "$LOCATION"               

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
--registry-login-server agwineacr.azurecr.io \
--registry-username agwineacr \
--registry-password $password  \
--target-port 5000 \
--ingress 'external' \
--query configuration.ingress.fqdn

#https://redwineapp.happyforest-21fb9d48.canadacentral.azurecontainerapps.io/

# References         
https://docs.microsoft.com/en-us/azure/container-apps/get-started?ocid=AID3042118&tabs=bash             