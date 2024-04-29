# ECS Fargate Cluster
AWS Fargate is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances

I don't pay here on running On-Demand Instances, only for Containers for service

* Monthly Cost of EC2 Instance with the same Instance type like Fargate more cheaper that ECS Fargate

To create Fargate Cluster Go to ECS Cluster --> Create Cluster --> Networking Only

You can run tasks from Fargate in any cluster, because he doesn't attach them with VPC 

Don't forget when you run task to choose Security group

In ECS Fargate Network Mode is always in awsvpc (Attaches Network Interface)

I created Security group with All traffic (You need only port 80 of your Container) before went to ECS Cluster

## Final Deployment