# VPC Bastion Host
Bastion hosts provide an external point of entry into a Virtual Private Cloud (VPC) network that contains VMs that don't have external IP addresses

## Demonstration

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Demonstration.png?raw=true">

First of All I created VPC with CIDR Block 192.168.0.0/16 and attached him to Internet Gateway

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/VPC-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Internet-Gateway.png?raw=true">

I created 2 Private and 2 Public Subnets in different Availvability zones,

Associate to Public Subnets IPv4 Addresses and also create 2 Route Tables: Public and Private and associate them to Subnets

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Subnets-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Route-Table-1.png?raw=true">

After that I started to work with Bastion Host, I created Security Group with SSH - port 22

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Security-group.png?raw=true">

Bastion should be in Auto-Scaling Group, So we need to create first Launch Template

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Launch-Template.png?raw=true">

Now I created Auto-Scaling Group, but I made a mistake, because I set Limit to Auto-Scaling Group to maximum 1 Instance, So I fixed after that

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/ASG-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/ASG-2.png?raw=true">

Now I checked EC2 Instance and we have our Bastion Host

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Instances-1.png?raw=true">

I connected to him with SSH protocol

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/SSH-Check-1.png?raw=true">

After that I wanted to see if my Bastion Host works correctly and I terminate them and Auto-Scaling Group run a new Instance in new Availability zone

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/Instances-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Bastion-Host/Screens/SSH-Check-2.png?raw=true">
