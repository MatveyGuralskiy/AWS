# ECS Service 
Service it's like Auto-Scaling Group for Containers in ECS, he store tasks and can be manage with Application Load Balancer

## Demonstration with Zero-Down Time
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Demonstration.png?raw=true">

I started with creating Security group with Inbound port 80 - HTTP

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Security-group.png?raw=true">

I used ECR Images for Classic Cluster

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/ECR.png?raw=true">

## Fargate Cluster

I created in ECS First Cluster Fargate Cluster

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Cluster-1.png?raw=true">

After this step I add Task Definitions for Clusters: ECR-Website, Simple-Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Task-Definition-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Task-Definition-2.png?raw=true">

The next step was to create Service for Fargate Cluster

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-4.png?raw=true">

I didn't create for him Application Load Balancer so my deployment was in Public IP's of Instances

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Container-Without-DNS.png?raw=true">

After that I removed my Fargate Cluster and created the new one but before it I created Application Load Balancer and Target Group

In Target Group I choose Target type: IP Addresses

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Target-group-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Target-group-2.png?raw=true">

And after that I created Application Load Balancer

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-ALB-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-ALB-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-ALB-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-ALB-4.png?raw=true">

So I already have been with ALB (Application Load Balancer) so I created new Fargate Cluster and Service

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-5-ALB.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-6.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-7.png?raw=true">

To check my new deployment of Containers I used DNS Name of Application Load Balancer

You can easily update your Containers and to control them go to Service --> Update

Choose the new Release

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-8-Update.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-9-Update.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Service-10.png?raw=true">

In Auto Scaling Group when You update Release it's the process:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-ALB-5-Update.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-ALB-6-Update.png?raw=true">

Deployment Updated version of Fargate-Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Fargate-Container-Update.png?raw=true">

## Classic Cluster

In Classic Cluster I used EC2 Instances and ECR Images

I created at the beginning Target Group

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Target-Groups.png?raw=true">

The next step was to create Application Load Balancer

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-ALB-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-ALB-2.png?raw=true">

It's my EC2 Instances for Classic Cluster

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-Instances.png?raw=true">

I created Classic Service

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-Service-1.png?raw=true">

It was my deployment for the first version

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-Container.png?raw=true">

After that I made some Update for Version of Containers

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-Service-2-Update.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-Service-3-Update.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-Service-4.png?raw=true">

What's happen in Application Load Balancer

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-ALB-3-Update.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-ALB-4-Update.png?raw=true">

My new version of Deployment of ECR Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Classic-Container-Update.png?raw=true">

My Clusters at the end

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Service/Screens/Clusters-Result.png?raw=true">
