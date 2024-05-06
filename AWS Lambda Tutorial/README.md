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