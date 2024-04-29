# ECS Fargate Cluster
AWS Fargate is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances

I don't pay here on running On-Demand Instances, only for Containers for service

* Monthly Cost of EC2 Instance with the same Instance type like Fargate more cheaper that ECS Fargate



You can run tasks from Fargate in any cluster, because he doesn't attach them with VPC 

Don't forget when you run task to choose Security group

In ECS Fargate Network Mode is always in awsvpc (Attaches Network Interface)

I created Security group with All traffic (You need only port 80 of your Container) before went to ECS Cluster

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Cluster/Screens-Cluster/Security-group.png?raw=true">

To create Fargate Cluster Go to ECS Cluster --> Create Cluster --> Networking Only

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Cluster-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Cluster-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Cluster-3.png?raw=true">

I also used for Tasks my ECR Images

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/ECR-Images.png?raw=true">

After that I created Task Definition for Fargate

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Task-Definition-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Task-Definition-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Task-Definition-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Task-Definition-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Task-Definition-5.png?raw=true">

After this step I created Tasks

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Tasks-1.png?raw=true">

I copy in container details the Public IP and saw my deployment of Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Container-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Tasks-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Container-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Container-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Container-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Container-5.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Tasks-3.png?raw=true">

All tasks list

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ECS_Fargate/Screens/Tasks-4-Final.png?raw=true">
