# VPC Peering
A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses

A VPC's can't be with the same CIDR Blocks

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Result.png?raw=true">

I created 3 VPC's:

- VPC Europe: eu-central-1 CIDR Block: 10.0.0.0/16

- VPC USA: us-east-1 CIDR Block: 172.16.0.0/16

- VPC Asia: ap-northeast-1 CIDR Block: 192.168.0.0/16

Europe VPC it's the main VPC which has 2 VPC Peerings between USA and Asia

VPC Europe has 2 Subnets:

- Public Subnet 10.0.10.0/24 with Internet Gateway and Route Table with access to Internet (Auto-assign to IPv4)

- Private Subnet 10.0.20.0/24 with Route Table local only

VPC USA has Private Subnet 172.16.10.0/24 and Route Table local only

VPC Asia has Private Subnet 192.168.10.0/24 and Route Table local only

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/VPC-Europe.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/VPC-USA.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Subnet-Europe.png?raw=true">

In every region, I created EC2 Instance, only in VPC Europe we have Public-IP and access to the Internet

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Instance-Europe.png?raw=true">

**I also created Security groups (firewall) in every region with SSH inbound and ICMP to all sources**

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/AWS-SG.png?raw=true">

After that I created new resource - Peering Connection in Europe VPC and send to every region (USA, Asia) requests and accept them

Don't forget to add in all Route Tables different CIDR Blocks, for example in Europe I added in Route Table CIDR Blocks: 172.16.0.0/16, 192.168.0.0/16

Model OSI:

1. Peering Connection it's Layer 1 in model OSI

2. Route Table it's Layer 3 in model OSI

In conclusion I connected to EC2 Instance of Europe VPC and make ping to Private-IP's of two different Instances of VPC USA and VPC Asia

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Result-Answer.png?raw=true">

## AWS Peering Connection
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Peering-Connection-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Peering-Connection-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Peering-Connection-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Peering-Connection-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Peering/Screens/Peering-Connection-5.png?raw=true">
