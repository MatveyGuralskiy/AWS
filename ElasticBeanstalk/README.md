# Elatic Beanstalk
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