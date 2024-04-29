# ECS Cluster
Before I started to work with ECS and create ECS Cluster, I ran EC2 Instance and Install to him docker and create with Dockerfile and index.html Docker Images and upload them to AWS ECR

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

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECR/Screens/Docker-Install-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECR/Screens/Docker-Install-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECR/Screens/Docker-Install-3.png?raw=true">

*How to Install AWS CLI for Ubuntu/Debian*
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

After that I make Images and Upload them

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Instance-ECR-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Instance-ECR-2.png?raw=true">

## Demonstration of ECS Cluster

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Demonstration.png?raw=true">

## Create Cluster
Create Security group for All Traffic for Docker Containers (ECS Tasks)

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Security-group.png?raw=true">

I went after everything to Clusters --> Create Cluster --> EC2 Linux + Networking

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Cluster-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Cluster-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Cluster-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Cluster-4.png?raw=true">

My Instances now and Auto-Scaling Group

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Instances-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Auto-Scaling-Group.png?raw=true">

Now create Task Definition for your Cluster to run Tasks

Choose CPU and Memory for your Instance type

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/AWS-Table.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Task-Definition-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Task-Definition-2.png?raw=true">

Finally you could run all tasks of Images:

I used 2 Images from my ECR

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/ECR-1.png?raw=true">

I created tasks of 2 versions and check in Details of Container which port they use and URL of Websites Applications

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Tasks-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Tasks-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Tasks-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Container-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Container-5.png?raw=true">

I also created task with nginx Image *nginx:latest*

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Container-3.png?raw=true">

And at the end I created tasks with 2 versions of my Images from DockerHub matveyguralskiy/simple_website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Tasks-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Container-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Container-2.png?raw=true">

## AWS Console at the end after all deploys

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Cluster-5-Final.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/develop/ECS_Cluster/Screens-Cluster/Instances-2.png?raw=true">
