# Elastic Beanstalk
Elastic Beanstalk is a service for deploying and scaling web applications and services. 
Upload your code and Elastic Beanstalk automatically handles the deployment—from capacity provisioning,
load balancing, and auto scaling to application health monitoring.

This service refers to CI/CD

You can create Infrastructure for your Web Application so fast, Elastic Beanstalk has Versioning

You also can do Green/Blue Deployment:

*Blue Deployment = Current Version of Web Application*

*Green Deployment = New version, make new Infrastructure and testing*

Platforms for Elastic Beanstalk: Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker(any platform can be in container)

Elastic Beanstalk controls with CloudFormation

## Deployment

I create 2 Environments for the Application "Web-Beanstalk": Production-A and Staging-B

In Production-A, I put the first version of the Application and made Deployment, after that I created new version of Application and put it to Staging-B environment

I made a Swap-Domain for to of them, so in Production we have Green/Blue Deployment of new Version

## Result demonstration

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Result.png?raw=true">
## Production-A
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/AWS-ElasticBeanstalk-Production.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Production-PHP.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Production-Website-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Production-Website-2.png?raw=true">

## Swap Domains of Production-A and Staging-B
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Swap-Domains-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Swap-Domains-2.png?raw=true">

## Staging-B
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/AWS-ElasticBeanstalk-Staging.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Staging-PHP.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Staging-Website-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/Staging-Website-2.png?raw=true">
<img src="">

## AWS Console CloudFormation and EC2 Instances

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/AWS-CloudFormation.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/ElasticBeanstalk/Screens/AWS-Instances.png?raw=true">
