# Elatic Beanstalk
Elastic Beanstalk is a service for deploying and scaling web applications and services. 
Upload your code and Elastic Beanstalk automatically handles the deployment—from capacity provisioning,
load balancing, and auto scaling to application health monitoring.

*.ebextensions = *.config files in directory .ebextensions*, allow to us make full customzining for Elastic Beanstalk:

- copy.config

- folders.config

Elastic Beanstalk run it with alphabet sorting A-Z

You can write configs in YAML or JSON

Commands:

- packages = download and install apps (yum, rpm, msi)

- sources = download and unzip archieve (tar, gzip, zip)

- files = create file (can download with "source")

- users = create users (only in Linux)

- groups = create groups (only in Linux)

- commands = run system commands before deployment

- container_commands = run system commands after deployment

- services = stop, start services

- Resources = use CloudFormation to create any resources in AWS

Environment variables = You can enter your secrets for Instances Environment

Immutable = like Green/Blue Deployment

Don't make in Elastic Beanstalk Database, because you can terminate it by mistake easily

## Result demonstration

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/Result.png?raw=true"/>

## Deployment Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/Website.png?raw=true"/>

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/Deployment-1.png?raw=true"/>

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/Deployment-2.png?raw=true"/>

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/Deployment-3.png?raw=true"/>

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/PHP-Template.png?raw=true"/>

## SSH Connection to AWS EC2 Instance
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/SSH-Connection.png?raw=true"/>

## AWS Console: EC2, Auto-Scaling-Group, LoadBalancer

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/AWS-Instances.png?raw=true"/>
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/AutoScaling-Group.png?raw=true"/>
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk_Ebextensions/Screens/LoadBalancer.png?raw=true"/>
