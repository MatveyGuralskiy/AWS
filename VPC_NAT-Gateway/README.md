# VPC NAT-Gatewway
A NAT gateway is a Network Address Translation (NAT) service. You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.

## Demonstration

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Demonstration.png?raw=true">

At the beggining I created VPC with CIDR Block 10.0.0.0/16

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/VPC-1.png?raw=true">

I attached to VPC Internet Gateway and create Public Subnets and Private Subnets in to Availability zones A, B

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Internet-Gateway.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Subnets-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Subnet-2.png?raw=true">

I associate every Route-Table to Subnets and create 2 Route-Tables for every Private Subnet

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Route-Table-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Route-Table-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Route-Table-3.png?raw=true">

Don't forget to edit Public Subnets for Associated IPv4 Adrresses and add to Public Route Table CIDR Block 0.0.0.0/0 (Internet) 

After that I went to NAT-Gateway and create 2 NAT-Gateways in Public Subnets in different Availability zones and attach them with Elastic IP's

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/NAT-Gateway-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/NAT-Gateway-2.png?raw=true">

Add every NAT-Gateway to Private Route-Tables

I also created Security group with port Inbound SSH - port 22

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Security-group.png?raw=true">

And run Instances in Public Subnet and Private Subnet

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/Instances.png?raw=true">

After everything I connected with SSH to Public Instance and with ssh protocol I connect to Private Subnet Instance with command *ssh -i KEY.pem USER@IP_ADDRESS* 

I checked with command *ping www.google.com* connection in Private Subnet Instance to Internet with NAT-Gateway 

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_NAT-Gateway/Screens/SSH-Connection.png?raw=true">
