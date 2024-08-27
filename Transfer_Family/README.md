# Transfer Family
AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services

It's basicly SFTP server without having to connect to AWS

SFTP, FTPS, FTP, AS2

Commands: cd, ls/dir, get (download), put (upload)

Tranfer Family can work with S3 and EFS

## Steps

1. Create S3 Bucket and Upload some files

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/S3-Bucket.png?raw=true">

2. Create SFTP Server in Transfer Family

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Transfer-Family-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Transfer-Family-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Transfer-Family-3.png?raw=true">

3. Add Route53 Domain

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Route53.png?raw=true">

4. Create IAM Role for Transfer Family to get access to S3 Buckets

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/IAM-Role-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/IAM-Role-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/IAM-Role-3.png?raw=true">

5. Generate ssh keys

```
ssh-keygen -f /PATH
```

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Linux-1.png?raw=true">

6. Add User

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Transfer-Family-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Transfer-Family-5.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Transfer-Family-6.png?raw=true">

7. Connect and test

```
sftp -i key-file USER@DOMAIN-ENDPOINT
```

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Transfer_Family/Screens/Linux-2.png?raw=true">
