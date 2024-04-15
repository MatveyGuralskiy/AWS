# CloudFront
CloudFront speed up static file load for Websites in different places in the world because of using cache saving "Edge caching"

I create S3 Bucket Static Website with ASL and make it public in Internet

You can make Geo-Restrict for countries you want for your Website (For example deny entry from Jordan)

To clean the cache use Invalidation

Default TTL cache is 86400 seconds = 24 hours

Also don't forget to set in Default Root Object --> index.html

## Map of CloudFront Edge Locations
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudFront/Screens/Map.png?raw=true" style = " width:1000px" />

## Website on S3 Bucket with CloudFront:
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudFront/Screens/S3-Bucket-Website-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudFront/Screens/S3-Bucket-Website-2.png?raw=true">

## AWS CloudFront
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudFront/Screens/AWS-CloudFront-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudFront/Screens/AWS-CloudFront-2.png?raw=true">
