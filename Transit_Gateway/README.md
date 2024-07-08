# Transit Gateway
Service works like VPC Peering, but we can minimize our Peerings between VPCs

I created 3 VPC with 3 Internet Gateways and 3 Instances

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/VPC.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Instance.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Internet-Gateway.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Route-Tables-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Security-group.png?raw=true">

Now I can create Transit Gateway

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Transit-Gateway.png?raw=true">

And we need attachments like Peerings between Transit Gateway and VPCs

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Transit-Gateway-Attachments.png?raw=true">

Automatically Transit Gateway creates Route Table for himself

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Transit-Gateway-Route-Table.png?raw=true">

After creation of Transit Gateway Service and his tools we should change our Route Tables of VPCs

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Route-Tables-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/Route-Tables-3.png?raw=true">

And I checked Ping between Instances in different VPC's

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/ping-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/ping-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transit_Gateway/Screens/ping-3.png?raw=true">
