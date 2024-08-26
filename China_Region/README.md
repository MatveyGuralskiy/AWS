# China Regions AWS
AWS has several regions in China, but they are operated differently from other AWS global regions. The key AWS regions in China are:

Beijing Region (cn-north-1): Operated by Sinnet.

Ningxia Region (cn-northwest-1): Operated by NWCD.

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/China_Region/Screens/China-1.jpg?raw=true">

China regions are full isolated from other AWS Regions, it means that your credentials not be available in AWS China

To open account in AWS China you must have business license, business should be located physically in China

The license called ICP from China Government, only after apply you may get access to ports 80, 8080, 443

If you got only Internal Access Account you will get only ports 22 and 3389 and S3 Bucket can't be Public

Due to Chinese regulations, the regions are managed by local providers under a specific licensing arrangement. While these regions offer many of the same AWS services, there are differences in availability, compliance, and operational practices compared to other AWS regions worldwide.

To use these regions, customers need a separate account specific to China, which is different from global AWS accounts.

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/China_Region/Screens/China-2.png?raw=true">

Example to Upload S3 Bucket Storage:

1. Copy all S3 Bucket Storage from different S3 Bucket and Region like Virginia for example:

```
aws s3 sync s3://matvey.com /home/temp --profile=MATVEY --region=us-east-1
```

2. Now upload it to S3 to AWS China

```
aws s3 sync /home/temp s3://matvey.cn --profile=MATVEYCHINA --region=cn-north-1
```
