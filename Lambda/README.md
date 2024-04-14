# AWS Lambda - Serverless technology
Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions.
Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement.

He makes automatically AutoScaling group, Can be work like event way without run resources for that (It's more cheaper than run Instances 24/7)

Lambda understand: Node.js, Java, C#, Python

Lambda can run with:
- AWS Console
- AWS CLI
- API Gateway
- Different events: like S3 bucket data change, DynamoDB update

Don't forget to access Cookies in your browser

in AWS IAM Create 2 Roles for Lambda:

IAM --> Roles --> Lambda --> Permission --> 1. S3 ReadOnlyAccess, 2. S3 FullAccess

## AWS Console Lambda
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda/Screens/AWS-Lambda-1.png?raw=true" style= "height:450px; width:900px" />
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda/Screens/AWS-Lambda-2.png?raw=true" style= "height:450px; width:900px" />
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda/Screens/AWS-Lambda-3.png?raw=true" style= "height:450px; width:900px" />

In terminal enter your AWS credentials, now you can work with 2 Lambda functions

## AWS CLI
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda/Screens/AWS-CLI-1.png?raw=true" style= "height:750px; width:900px" />
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda/Screens/AWS-CLI-2.png?raw=true" style= "height:550px; width:900px" />
