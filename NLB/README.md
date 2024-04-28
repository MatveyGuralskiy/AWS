# Network Load Balancer
The Network Load Balancing (NLB) feature distributes traffic across several servers by using the TCP/IP networking protocol.

For this example, I created 2 Webservers with Security group and attach them to Target Group

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/NLB/Screens/Instances.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/NLB/Screens/TargetGroup.png?raw=true">

We also need to create Elastic IP before

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/NLB/Screens/ElasticIP.png?raw=true">

After everything I created Network Load Balancer and attach Target Group with Elastic IP in one Availability zone

Now the dns link of Network Load Balancer works for 2 Instances

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/NLB/Screens/NLB-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/NLB/Screens/NLB-2.png?raw=true">

## Result of NLB

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/NLB/Screens/Website-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/NLB/Screens/Website-2.png?raw=true">



