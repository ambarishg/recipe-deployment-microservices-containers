aws ecr create-repository --repository-name redwine-repo 

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 113170463366.dkr.ecr.us-east-1.amazonaws.com

docker tag redwine:latest 113170463366.dkr.ecr.us-east-1.amazonaws.com/redwine-repo:latest