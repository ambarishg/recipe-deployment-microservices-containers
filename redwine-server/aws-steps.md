# Create the Repository in ECR
aws ecr create-repository --repository-name redwine-repo 

# Get the Login and Password for the ECR Repository
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 113170463366.dkr.ecr.us-east-1.amazonaws.com

# Tag the docker container image
docker tag redwineflask:latest 113170463366.dkr.ecr.us-east-1.amazonaws.com/redwine-repo:v1

# Push the image into the  ECR Repository
docker push 113170463366.dkr.ecr.us-east-1.amazonaws.com/redwine-repo:v1

<hr/>


# Create the EKS cluster
eksctl create cluster \
--name agredwine \
--region us-east-1 

# Update the kubeconfig
aws eks --region <region-code> update-kubeconfig --name <cluster_name>
aws eks --region us-east-1 update-kubeconfig --name agredwine

# Creating the mandatory resources for NGINX Ingress in the cluster            
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-0.32.0/deploy/static/provider/aws/deploy.yaml           

`The above manifest file also launches the Network Load Balancer(NLB).`      

# Run the YAML
kubectl apply -f redwine-eks-ingress.yaml

# Get the loadbalancer URL          
export loadbalancer=$(kubectl get svc redwine-service -o jsonpath='{.status.loadBalancer.ingress[*].hostname}')              
curl -m3 -v ${loadbalancer}           
curl -L -v ${loadbalancer}       
curl -k -s http://${loadbalancer}        
curl -vv ${loadbalancer}     

# Delete the cluster
eksctl delete cluster --name <prod>
eksctl delete cluster --name agredwine
