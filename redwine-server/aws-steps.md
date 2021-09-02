aws ecr create-repository --repository-name redwine-repo 

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 113170463366.dkr.ecr.us-east-1.amazonaws.com

docker tag redwineflask:latest 113170463366.dkr.ecr.us-east-1.amazonaws.com/redwine-repo:v1

docker push 113170463366.dkr.ecr.us-east-1.amazonaws.com/redwine-repo:v1

eni-0e50a3b2382dac4d1
aws ec2 describe-network-interfaces --network-interface-ids eni-xxxxxxxx
aws ec2 describe-network-interfaces --network-interface-ids eni-xxxxxxxx

redwinealb-1263944540.us-east-1.elb.amazonaws.com
