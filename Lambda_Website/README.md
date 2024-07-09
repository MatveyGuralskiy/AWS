# Simple Website with Lambda
The Website will be able to run only when client need it (when he goes to this website)

Create Lambda function and attach in Advanced Options Lambda URL

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Website/Screens/Lambda-1.png?raw=true">

Use Python code *script.py* from directory

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Website/Screens/Lambda-1.png?raw=true">

Now create Certificate SSL in Certificate Manager

Create CloudFront distribution for Serverless Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Website/Screens/CloudFront-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Website/Screens/CloudFront-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Website/Screens/CloudFront-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Website/Screens/CloudFront-4.png?raw=true">

Now add in Route53 Record alias with CloudFront

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Website/Screens/Route53.png?raw=true">

Now Serverless website will work in domain name *lambda.matveyguralskiy.com*
