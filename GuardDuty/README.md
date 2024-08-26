# GuardDuty - Cloud Cyber Security
GuardDuty is designed to automatically manage resource utilization based on the overall activity levels within your AWS accounts, workloads, and data. GuardDuty adds detection capacity only when necessary and reduces utilization when capacity is no longer needed.

Analize CloudTrail Logs, VPC Logs, DNS Logs

Used ML to discover potentionally activity

Has list of suspicious IP Addresses

Can tell you for example if someone change Permissions/Policies for himself, If EC2 has Mining Bitcoin or some Software on him, If someone use a new Region in Account

Can show you Location, IP addresses and etc information of user activity

You could attach Trusted IP addresses and Treats

Attach SNS Topic and EventBridge Rule

In my example I created SNS Topic with EventBridge Rule which looks at GuardDuty Findings

I Enable GuardDuty

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/GuardDuty-1.png?raw=true">

I created SNS Topic

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/SNS.png?raw=true">

And Add EventBridge Rule

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/EventBridge-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/EventBridge-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/EventBridge-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/EventBridge-4.png?raw=true">

Now I clicked on Generate Sample Finding to check if EventBridge works correctly

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/GuardDuty-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/GuardDuty-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/GuardDuty-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/GuardDuty-5.png?raw=true">

I get on Gmail some Notifications:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/GuardDuty/Screens/Email.png?raw=true">
