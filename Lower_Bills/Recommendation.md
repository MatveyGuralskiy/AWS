# How to lower bills of AWS
When you start a new job, check out Amazon resources, do some analysis procees of Infrastructure, which Amazon services most used, calculate them, almost always you can lower your bills and save money for your company

Recommendations: 

- Use AWS Pricing Calculator or AWS Simple Calculator

- Check Billing Dashboard to see the biggest changes of account per services, per regions

- RDS Instance size-check Utilization CPU/Memory in last month

- EC2 Instances size-check Utilization CPU/Memory in last month

- Reserved Instances for EC2 and RDS (not hourly, reserve for a year for example)

- AWS Instance Scheduler (Stop Instances and turn on only at a hour when a job is running)

- Old EBS Snapshots

- Unattached EBS Volumes

- Old AMI

- Unattached Elastic IP

- CloudFront Price Class, (Check if you have customers in Asia, South America, Australia)

- S3 Storage Class for files we don't use frequently

- Unattached Load Balancer, empty Target Group

- Do we need NAT Gateway?

- Replace SSL Certificate to AWS Certificate Manager SSL