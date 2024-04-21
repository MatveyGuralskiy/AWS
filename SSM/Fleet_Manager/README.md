# System Manager - Run Command
Servers should have an IAM Role of SSM 

After you ran EC2 Instance, attach the Role "AmazonEC2RoleforSSM" to your resource and go to System Manager --> Fleet Manager

## Attach IAM Role of SSM to the Instance
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-IAM-Role.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-Instance-Attach.png?raw=true">

SSM Agent already installed in Ubuntu in AWS, but distributions like Amazon Linux, CentOS, Red Hat should download and install SSM Agent, go to Amazon documentation and follow the instruction

<br>
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-Instance-3.png?raw=true">

## Amazon Documentation [LINK](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-al2.html")
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/SSM-Agent-Amazon-Linux.png?raw=true">

Now write a bash script for your Instances to run commands in SSM Console AWS

Actions --> Run command --> RunShellScript

## Results of System Manager Console
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-SSM-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-SSM-2.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-SSM-3.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-SSM-4.png?raw=true">

## AWS Instance
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-Instance-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Fleet_Manager/Screens/AWS-Instance-2.png?raw=true">
