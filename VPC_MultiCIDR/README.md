# VPC Multi-CIDR
You can optionally associate additional IPv4 CIDR blocks and one or more IPv6 CIDR blocks

The Maximum number of CIDR Blocks in VPC can be 5

AWS always takes 5 IP addresses from subnet

You can add not only RFC 1918 addresses (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 = RFC 1918)

## VPC Result Demonstration

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/Result-Demonstration.png?raw=true">

For example I created VPC with CIDR Block 10.0.0.0/16 (65536 addresses) with Internet-Gateway and Route Table, access to the Internet

Don't forget to attach in Route Table 0.0.0.0/0 CIDR and Enable Auto-assigned IPv4 

I added 2 Subnets: 

- Subnet-A 10.0.0.0/7 (32768 addresses) in availability zone a

- Subnet-B 10.0.128.0/7 (32768 addresses) in availability zone b

Now our VPC IP addresses are full, so we can increase VPC:

Choose your VPC --> Actions --> Edit CIDR's --> Add CIDR IPv4

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/VPC-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/VPC-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/VPC-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/VPC-4.png?raw=true">

I added new CIDR Block 10.1.0.0/16, so we have 65536 new addresses for our VPC

I created additional Subnets:

- Subnet-C 10.1.0.0/7 (32768 addresses) in availability zone a

- Subnet-D 10.1.128.0/7 (32768 addresses) in availability zone b

In Route-Table automatically you have attached new CIDR Block

After that I created 2 Instances in different Subnets and Availability zones

At the final I have 131072 IP-Addresses for one VPC

I connect to one of the Instances with CIDR Block 10.0.0.0/7 with Public-IP and made ping to Instance with CIDR Block 10.1.0.0/7 with Private-IP 

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/Result-Instances.png?raw=true">

## AWS Console: Subnets, Internet-Gateway, Instances

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/Subnet-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/Subnet-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/Internet-Gateway.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_MultiCIDR/Screens/Instances.png?raw=true">
