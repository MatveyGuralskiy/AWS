# CodeDeploy Service
Is a managed service that automates the deployment of applications to various computing resources such as EC2 servers, ECS, Lambda and OnPremises

I created first of all EC2 Instance with Apache Server with bootstrapping *script.sh*

I also installed CodeDeploy Agent

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/Instance-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/Instance-2-Apache.png?raw=true">

For CodeDeploy we need to attach IAM Role

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/IAM-1-Instance.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/Instance-3-IAM.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/Instance-4-IAM.png?raw=true">

Now we need to restart our server

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/Instance-5-Restart.png?raw=true">

Let's start to work with CodeDeploy service, we need to create IAM role

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/IAM-2-CodeDeploy.png?raw=true">

Go to Service CodeDeploy and create Application

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-1.png?raw=true">

Create for Application Deployment group

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-5.png?raw=true">

Let's create SNS topic for Deployment

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/SNS-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/SNS-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/SNS-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/SNS-4.png?raw=true">

And attach it in CodeDeploy Application

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-8-SNS.png?raw=true">

We need to Create GitHub repository and upload all files:

appspec.yml - for CodeDeploy

index.html - Application

scripts - directory with stages for CodeDeploy

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/GitHub.png?raw=true">

Copy a commit from your Git of your GitHub repository

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/Git.png?raw=true">

And now we can create Deployment with GitHub

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-9-Deploy.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-10-Deploy.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/CodeDeploy-11-Deploy.png?raw=true">

This is the result of Deployment:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy/Screens/Website.png?raw=true">
