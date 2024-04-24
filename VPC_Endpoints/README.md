# VPC Endpoints
Without a VPC endpoint, you would have to access the S3 bucket over the internet, which can be a security risk. With a VPC endpoint, you can access the S3 bucket directly from your VPC without ever leaving the private network

To make access to S3 Bucket and SSM for Private Subnet we need to use Endpoints

Endpoints it's like holes in network, VPC it's isolated network by default

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Result.png?raw=true">



First of All I created VPC 10.0.0.0/16 with Public Subnet 10.0.10.0/24 and Internet-Gateway with Auto-Assigned IPv4, and Route Table with 0.0.0.0/0 access (Internet)

Private Subnet was 10.0.20.0/24

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/VPC-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Internet-Gateway.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/RouteTable-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Subnets-1.png?raw=true">

In every subnet I ran Instance with Amazon Linux OS, and created Security group with SSH, HTTP, HTTPS

I created IAM Role for Instances to S3 with Full Access and SSM for EC2

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Instances-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Instances-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/IAM-Role-Attach.png?raw=true">

After that I'm connected to the Public Instance with Public Subnet and run command:

aws s3 ls - to see the list of S3 Buckets, If it works it means the Role works and we get access to the Internet

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Instance-Connect-1.png?raw=true">

But This command doesn't work in Private Subnet, so we should add Endpoints to Network Interface of Private Instance:

The first Endpoint get access to S3 Bucket Gateway, The second Endpoint get access to System Manager which connects with port 443 (HTTPS) because of Security group

To add Endpoints Go to VPC --> Endpoints --> Choose Service s3 --> Add to Public and Private Subnet

Make the same with Services SSM and EC2Messages to get access to System Manager to work with EC2 Instances

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Endpoints-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Endpoints-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Endpoints-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Endpoints-4.png?raw=true">

Now after I created everything I'm back to my Public Instance and connect with ssh key to Private Instance and command "aws s3 ls" work

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/Instance-Connect-2.png?raw=true">

## SSM Fleet Manager

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/SSM-Fleet-Manager-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPC_Endpoints/Screens/SSM-Fleet-Manager-2.png?raw=true">
