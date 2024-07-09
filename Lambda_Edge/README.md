# Lambda-Edge
provide to expand opportunities for CloudFront

Lambda must be created in Virginia region!

We can work with our request in 4 stages of different status requests

1. Viewer Request - when CloudFront gets request from a client

2. Origin Request - before CloudFront sends request to Origin(EC2, S3, ALB)

3. Origin Response - when CloudFront gets response from Origin(EC2, S3, ALB)

4. Viewer Response - before CloudFront sends response to client

Examples to Use:

1. We can check Headers of requests and shows different pages

2. We can ask for Username and Password before loading a page

and more

My example:

1. Create S3 Bucket, Upload file, Create also Certificate SSL in Certificate Manager, Create CloudFront directory and Route53 Record (full tutorial: https://github.com/MatveyGuralskiy/AWS/tree/main/Static_Website)

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Edge/Screens/CloudFront.png?raw=true">

2. Create IAM role for lambda: lambdaBasicExecutionRole and edit the role in trust relationships:

```
"Service": [
    "lambda.amazonaws.com",
    "edgelambda.amazonaws.com"
]
```

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Edge/Screens/IAM_Role.png?raw=true">

3. Create Lambda function in Virginia and after Deploy click on Actions --> Deploy to Lambda@edge

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Edge/Screens/Deploy%20to%20Lambda@Edge.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Edge/Screens/Lambda_Function.png?raw=true">

4. Go to the Website and checked if it works correctly, open it in different browser or with Incognito mode

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Edge/Screens/Website-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_Edge/Screens/Website-2.png?raw=true">
