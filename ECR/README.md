# ECR - Elastic Container Registry
ECR is an AWS managed container image registry service that is secure, scalable, and reliable

It's storage of images like DockerHub

First of all I created Security group with ports SSH and HTTP and EC2 Instance *Docker Ubuntu*

I Install to Instance Docker and AWS CLI

*How to Install Docker for Ubuntu/Debian*

```
sudo apt update
sudo apt install apt-transport-https
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce
sudo systemctl status docker
sudo usermod -aG docker $USER
```

*How to Install AWS CLI for Ubuntu/Debian*
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

After that I export my AWS Credentials with environment variables and went to AWS Console

ECR Service --> Create Repository --> Copy the URI link

I come back to the Instance SSH connection and in console enter this command to connect to the ECR with docker:

```
aws ecr get-login-password --region YOUR_REGION | docker login --username AWS --password-stdin YOUR_AWS_USER_ID.dkr.ecr.YOUR_REGION.amazonaws.com
```

I used Dockerfile and index.html for Docker Image:

```
docker build -t website:V1 .
docker tag website:V1 YOUR_URI_LINK_ECR:V1
docker images
docker push YOUR_URI_LINK_ECR:V1
# Created new version of Image Version 2
docker build -t website:V2 .
docker tag website:V1 YOUR_URI_LINK_ECR:V2
docker images
docker push YOUR_URI_LINK_ECR:V2
# To download the Docker Image
docker pull YOUR_URI_LINK_ECR:V1 (or V2)
# To run the Docker Container
docker -d -p YOUR_PORT:80 website:V1 (or V2)
```