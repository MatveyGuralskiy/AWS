# API Gateway
AWS API Gateway accepts and routes requests to the desired services

## Serverless API Gateway
We are going to create 3 Lambda functions with API Gateways, Route53 Record, Certificate SSL and API Gateway Custom Domain Name with Mapping

First of all I created 3 Lambda functions

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Lambda-1.png?raw=true">

The next step was to create API Gateways

I created API Gateway REST API with Method GET and made Deploy API

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Gateway-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Gateway-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Gateway-3-Method.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Gateway-4-Deploy.png?raw=true">

I also created Certificate SSL in Certificate Manager

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Certificate-Manager.png?raw=true">

Now we need to create API Custom Domain Name and attach mapping

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Custom-Domain-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Custom-Domain-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Custom-Domain-3-Mapping.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Custom-Domain-4-Mapping.png?raw=true">

When we finished to do that we can see that our Mapping API Gateways Default Domains are active, we need to inactive them

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Custom-Domain-5-Mapping.png?raw=true">

Go to Settings of every API Gateway and inactive Default Domain Name

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Default-DNS-Inactive-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Default-DNS-Inactive-2.png?raw=true">

Now to save changes we need to deploy every API Gateway

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/API-Default-DNS-Inactive-Deploy-3.png?raw=true">

It's how one of Lambda functions looks like

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Lambda-3-Result.png?raw=true">

Add in Route53 Record alias for API Gateway

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Route53.png?raw=true">

## Result

### Website main page:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Main=1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Main=2.png?raw=true">

### Website films page:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Films-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Films-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Films-3.png?raw=true">

### Website quote page:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Quote-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Quote-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/API_Gateway/Screens/Website-Quote-3.png?raw=true">
