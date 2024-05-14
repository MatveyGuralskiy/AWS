# Static Website with S3 Bucket + CloudFront
Steps:
- [ ] Create HTML Page
- [ ] Create S3 Bucket, Upload Application
- [ ] Create Certificate Manager with DNS Validation
- [ ] Create CloudFront distribution
- [ ] Create Record in Route53

## Demonstation

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/Demonstration.png?raw=true">

## Steps:

First of All create Application for example with HTML and CSS

Go to AWS Console and Create S3 Bucket with the same name as DNS Name you want to set for your Website

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/S3-Bucket-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/S3-Bucket-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/S3-Bucket-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/S3-Bucket-4.png?raw=true">

Now we need to attach SSL Certificate for our Website to get HTTPS

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/Certificate-Manager-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/Certificate-Manager-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/Certificate-Manager-3.png?raw=true">

Upload files of your Website to the S3 Bucket you already created

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/S3-Bucket-5-Upload.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/S3-Bucket-6.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/S3-Bucket-7.png?raw=true">

The next step is to create CloudFront distribution

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/CloudFront-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/CloudFront-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/CloudFront-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/CloudFront-4.png?raw=true">\

In Route53 Attach your DNS Name with Alias CloudFront

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/Route-53.png?raw=true">

And the result of your Website in DNS name we choose

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Static_Website/Screens/Website.png?raw=true">
