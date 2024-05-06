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