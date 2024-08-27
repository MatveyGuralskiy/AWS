# Transfer Family
AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services

It's basicly SFTP server without having to connect to AWS

SFTP, FTPS, FTP, AS2

Commands: cd, ls/dir, get (download), put (upload)

Tranfer Family can work with S3 and EFS

## Steps

1. Create S3 Bucket and Upload some files

<img src="">

2. Create SFTP Server in Transfer Family

<img src="">

3. Add Route53 Domain

<img src="">

4. Create IAM Role for Transfer Family to get access to S3 Buckets

<img src="">

5. Generate ssh keys

<img src="">

6. Add User

<img src="">

7. Connect and test

<img src="">