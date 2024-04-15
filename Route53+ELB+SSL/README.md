# Route53 with Elastic LoadBalancer and SSL Certificate
Steps:

1. First of All I went to Certificate Manager and create SSL/TLS Certificate with DNS validation

2. After that I went to the new SSL/TLS Certificate I created and click on Create Route53

3. Now we should run LoadBalancer with 2 Instances and Website, I write terraform code for that -->   https://github.com/MatveyGuralskiy/Terraform/tree/main/LoadBalancer

4. Now we attach our new LoadBalancer to the Route53, Create Record Set as Type A, Alias (Yes) and choose your ELB

5. Go to you new static Subdomain, now it have to be secure

## Website result with ELB

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53+ELB+SSL/Screens/Website-1.png?raw=true"/>

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53+ELB+SSL/Screens/Website-2.png?raw=true"/>

## AWS Console: ELB, Route53, EC2

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53+ELB+SSL/Screens/AWS-ELB.png?raw=true"/>

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53+ELB+SSL/Screens/AWS%20Route53.png?raw=true"/>

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Route53+ELB+SSL/Screens/AWS-Instances.png?raw=true"/>
