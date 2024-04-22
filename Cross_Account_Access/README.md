# Cross Account Access
If you have a developers which want to connect to AWS user and get S3 Bucket files you can use Cross Account Access

Go to your developer user information and copy the Account ID

Now in IAM Roles, create new role for Another AWS account and paste the Account ID of Developer

Get him S3ReadOnly role to use the files in S3 Bucket

In Trust Relationship you can choose the users you want to get the Cross Account Access

root = means the Cross Account Access gives to all users of this account

## AWS IAM Role
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Cross_Account_Access/Screens/AWS-IAM-Role-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Cross_Account_Access/Screens/AWS-IAM-Role-2.png?raw=true">

## AWS CLI
Now go to developer console and download aws cli

```
aws iam get-user = to check whats your current user, like command whoami in linux

aws sts assume-role --role-arn "ARN ROLE OF ADMIN" --role-session "NameOfSession"

#Copy Access Key id, Password and Token

#export(linux) or set(windows) to add environment variables to OS

export AWS_ACCESS_KEY=YOUR_ACCESS

export AWS_SECRET_ACCESS_KEY=YOUR_KEY

export AWS_SESSION_TOKEN=YOUR_TOKEN

```

Or you can give link to your developer to enter it in his browser and get Cross Account Access

In short:

1. In Trust Relationship of IAM Role you write who and from which account can be able to use the Role

2. What's account get the access have to make Assume Role and get temporary Credentials


<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Cross_Account_Access/Screens/AWS-CLI.png?raw=true">
