az aks create \
    --resource-group winegroup \
    --name wineAKSCluster \
    --node-count 1 \
    --generate-ssh-keys \
    --attach-acr agwineacr

<!-- az aks get-credentials --resource-group myResourceGroup --name myAKSCluster -->
az aks get-credentials --resource-group winegroup --name wineAKSCluster

kubectl apply -f redwine-azure.yaml

