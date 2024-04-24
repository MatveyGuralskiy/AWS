# Route53 Health Check
Health checks are a way of asking a service on a particular server whether or not it is capable of performing work successfully

I create two Instances with Boot-straping *script.sh* and created Webserver, attached before Security groups with HTTP port access

The Instances placed in Paris and London regions

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Instance-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Instance-2-London.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Instance-3-Paris.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Security-group.png?raw=true">

## Webservers:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Webserver-London.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Webserver-Paris.png?raw=true">



After I checked that every Webserver works correctly I went to Route53

To create Health Check: Route53 --> Heatlh Checks --> Endpoint --> IP address without Host name, path "/index.html" --> Create alarm SNS

For example I wrote:

- SNS Topic: Webserver-London_Down

- mail: YOUR_EMAIL

If we get 3 failure threshold we get a mail message

I created 2 Health Checks and Apply subscription in my email

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/HealthCheck-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/HealthCheck-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/HealthCheck-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Subsribe-1.png?raw=true">

After this step I stopped Instance in Paris and wait to the message in AWS Console and in email

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Instance-4-Paris-Stop.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53_Health_Check/Screens/Subsribe-2.png?raw=true">
