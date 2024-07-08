# Secrets Manager
Every time you want to store credentials for Databases AWS reccomends to use Secrets Manager Service

You pay for every secret

Secrets might be changed every N days for example every 7 days

You can store many secrets in one secret because of JSON format

SSM Parameter Store can store your credentials for free!

## Example

I created 2 secrets: the first one is with couple of secrets in one with JSON format, and the second one is just a random token

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Secrets_Manager/Screens/Secret-Manager-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Secrets_Manager/Screens/Secret-Manager-2.png?raw=true">

AWS CLI:
```
# list of secrets:
aws secretsmanager list-secrets

# To see information of secret:
aws secretsmanager get-secret-value --secret-id NAME(for example: dev/aws_training/token)

# To see secret value:
aws secretsmanager get-secret-value --secret-id NAME(for example: dev/aws_training/token) --output text --query 'SecretString'

# To see secret value for JSON:
aws secretsmanager get-secret-value --secret-id NAME(for example: dev/aws_training/token) --output text --query 'SecretString' | jq -r .SECRET_NAME(for example: DB_PASSWORD)
```

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Secrets_Manager/Screens/CLI-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Secrets_Manager/Screens/CLI-2.png?raw=true">
