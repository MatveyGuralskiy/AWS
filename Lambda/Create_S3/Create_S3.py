import boto3, os, time
AWS_DEFAULT_REGION = "eu-west-3"
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION
bucketName = "lambda-created-me-on-" + str(int(time.time()))
def lambda_handler(event, context):
    myS3 = boto3.resource('s3')
    try:
        results = myS3.create_bucket(
            Bucket = bucketName,
            CreateBucketConfiguration = {'LocationConstraint': AWS_DEFAULT_REGION}
        )
        return ("<h1>S3 Bucket Created Successfully </h1><br><br>" + str(results))
    except:
        return ("<h1>Error</h1><br><br>")
    