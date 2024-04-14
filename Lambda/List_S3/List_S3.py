import boto3, os
def lambda_handler(event, context):
    myS3 = boto3.client('s3')
    try:
        results = myS3.list_buckets()
        print(results)
        output = ""
        for bucket in results['Buckets']:
            output+=bucket['Name']+"<br>"
        return ("<h1>S3 Bucket List of Names:</h1><br><br>" + output)
    except:
        return ("<h1>Error</h1><br><br>")