# Lambda with Application Load Balancer

If we get million request per second, ALB will create million Lambda function and it will be much cheaper than API Gateway

Step 1: Create Lambda function

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/Lambda-1.png?raw=true">

Step 2: Create Certificate SSL in Certificate Manager

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/Certificate_SSL.png?raw=true">

Step 3: Create Security group with HTTP and HTTPS ports

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/SG.png?raw=true">

Step 4: Create Target group for Lambda function with Health Check

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/TG-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/TG-2.png?raw=true">

Step 5: Create ALB with ports 80 and 443 (attach certificate)

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/ALB-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/ALB-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/ALB-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/ALB-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/ALB-5.png?raw=true">

Step 6: Edit Redirect in port 80

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/ALB-6-Redirect.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/ALB-7-Redirect.png?raw=true">

Step 7: Create Route53 Record for ALB

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/Route53.png?raw=true">

This is how our Lambda function looks like:

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/Lambda-2.png?raw=true">

See the result of Lambda Function

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/Website-1.png?raw=true">

Now change URL attach to Domain name/?name=YOUR_VALUE

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_ALB/Screens/Website-2.png?raw=true">
