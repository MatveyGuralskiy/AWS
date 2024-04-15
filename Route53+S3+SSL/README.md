# Route53 with S3 Bucket and SSL Certificate
Steps:

1. First of All I went to Certificate Manager and create SSL/TLS Certificate with DNS validation

2. After that I went to the new SSL/TLS Certificate I created and click on Create Route53

3. Now we should create S3 Bucket and make them public, upload your Website file (You can upload in directory *Website* the index.html file to your S3 Bucket)

4. Now we attach our new S3 Bucket to the Route53, Create Record Set as Type A, Alias (Yes) and choose your new Subdomain

5. Go to you new static Subdomain, now it have to be secure

## Result demonstration

## Website

## AWS S3 Bucket

## AWS Console CloudFront, Route53