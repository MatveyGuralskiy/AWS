# AppRunner
AppRunner provide to you fast and easily deploy your application from GitHub, ECR, Bitbucket

Automatically deploy if code was changed (new commit), could create Load Balancer, Scaling, create SSL Certificate, Route53 Record also

This service more simply than Elastic Beanstalk

App Runner used Docker-Fargate

My Example:

1. Create GitHub Repository, use my Application_Repository directory (with apprunner.yaml for build configuration)

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/GitHub.png?raw=true">

2. Create App Runner Service (Automatic cost 1$ in month)

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-5.png?raw=true">

This is the Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-1-V1-Without-DNS.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-2-V1-Without-DNS.png?raw=true">

3. Add Custom Domain for Service, he will create Route53 Records and SSL Certificate automatically

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-6-DNS.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-7-DNS.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-8-DNS.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-9-DNS.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-10-DNS.png?raw=true">

Check new Domain name of Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-3-V1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-4-V1.png?raw=true">

4. Update Version of Application and App Runner will automatically run new Build for Deployment

Clone Repository and Change files for version 2 of Application

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Git-V2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-11-V2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-12-V2.png?raw=true">

New Version of Application

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-5-V2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-6-V2.png?raw=true">

5. Choose configration file now

Now let's change our configuration to configuration file from GitHub repository *apprunner.yaml*

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-13-Config-file.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-14-Config-file.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-15-Config-file.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-16-Config-file.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-17-Config-file.png?raw=true">

6. Test it, create Version 3 of Application

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Git-V3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-17-V3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-18-V3.png?raw=true">

This is Version 3 Application Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-7-V3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/Website-8-V3.png?raw=true">

Our Service App Runner

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/App_Runner/Screens/AppRunner-19-Service.png?raw=true">
