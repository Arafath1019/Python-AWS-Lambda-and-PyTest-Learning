## Reading File content from S3 on Lambda Trigger
```
import boto3
def lambda_handler(event, context):
    s3 = boto3.client("s3")

    if event:
        print("Event", event)
        file_obj = event["Records"][0]
        filename = str(file_obj["s3"]["bucket"]["key"])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket="bucket-name", Key=filename)
        print("File Obj: ", fileObj)
        file_content = fileObj["Body"].read().decode("utf-8")
        print("File Content", file_content)
    
    return "Return from lambda"
```

## Setting cron job on lambda
1. Add CloudWatch Evevnts as trigger in lambda function
2. Configure the CloudWatch Events as below
- set name for the event
- set a new role for this
- set role type as Schedule expression like rate(1 day), rate(1 minute) etc

## Invoke lambda function from another lambda function

Lambda Function1:
```
import boto3, json
def lambda_handler(event, context):
    invokelam = boto3.client("lambda", region_name="us-east-1")
    payload = {"message": "Hi, you have been invoked"}
    response = invokelam.invoke(FunctionName="lambda_function2", InvocationType="RequestResponse", Payload=json.dumps(payload))
    print(response["payload"].read())
    return "Hello from lambda"
```

Lambda Function2:
```
def lambda_handler(event, context):
    print(event)
    return "Return from lambda function2"
```

## Upload file from Lambda function to S3 bucket
lambda_handler function:
```
import json
import boto3
import pprint from pprint

def lambda_handler(event, context):
    client = boto3.client("ec2")
    s3 = boto3.client("s3")

    status = client.describe_instance_status(IncludeAllInstances = True)
    with open("/tmp/log.txt", "w") as f:
        json.dumps(status, f)
    
    s3.upload_file("/tmp/log.txt", "s3-bucket-name", "logs.txt")

    for i in status["InstanceStatuses"]:
        print("AvailabilityZone : ", i["AvailabilityZone"])

    return {
        "statusCode": 200,
        "body": json.dumps("Hello from lambda")
    }
```

## Upload data to S3 without saving to file via lambda function
```
import json
import boto3
from pprint import pprint

def lambda_handler(event, context):
    client = boto3.client("ec2")
    s3 = boto3.client("s3")
    status = client.describe_instance_status(IncludeAllInstances=True)

    s3.put_object(Bucket="s3_bucket_name", Key="data-log.txt", Body=str(status))

    return {
        "statusCode": 200,
        "body": json.dumps("Hello from lambda")
    }
```