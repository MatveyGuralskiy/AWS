# System Manager - Parameter Store
Parameter Store - here you can store your secrets and can use them (also if you change the secrets value they will update) for your resources in AWS

Before that you should go the IAM Role and add new role for EC2 - for Simple System Manager

And attach him to the EC2 Instance: Actions --> Security --> Modify IAM role

I create for example username *DB-username* and password *DB-password*

## AWS SSM Console
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Parameter_Store/Screens/AWS-SSM.png?raw=true">

## Results of Secrets in Instance
To export them to your Instance use command
*aws ssm get-parameters --name NAME_SECRET --region REGION_NAME --output text --query Parameters[].Value*


<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Parameter_Store/Screens/Parameter-Store-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Parameter_Store/Screens/Parameter-Store-2.png?raw=true">
