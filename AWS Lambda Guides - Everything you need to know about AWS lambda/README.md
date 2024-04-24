# AWS Lambda Guides

## AWS Lambda Introduction
- Run functions on demand without the server
- Supports many languages (python, java, c#, go, ruby, js)
- Adhoc tasks or completely serverless high TPS applications
- Pay per invocation, duration, memory
- Built in metrics with AWS Cloudwatch

## How lambda works
<img src="images/1.png" alt="Networking 1" height="200" width="700">

## Why is it so popular?
- Integrations with other AWS services
- API Gateway -> lambda(REST APIs)
- S3 -> lambda (Data processing)
- SQS -> lambda (Message Buffering & Processing)
- SNS -> lambda (Message Processing)
- Step functions -> lambda (Workflow Orchestration)
- DynamoDB -> lambda (Change Detection)

## Invoke AWS Lambda function from another Lambda function
<img src="images/2.png" alt="Networking 1" height="300" width="700">

- ARN(Amazon Resource Name) - ARN is important to call an aws service

LambdaToInvoke Function:
```
import json
import uuid

def lambda_handler(event, context):
    customerId = event["CustomerId"]
    transactionId = str(uuid.uuid1())

    return { "CustomerId": customerId, "Success": "true", "TransactionId": transactionId }
```

Invoker Function:
```
import json
import boto3

client = boto3.client("lambda")

def lambda_handler(event, context):
    inputForInvoker = { "CustomerId": "123", "Amount": 50 }

    response = client.invoke(
        FunctionName="ARN-link-of-LambdaToInvoke-function",
        InvocationType="RequestResponse" # Event Type
        Payload=json.dumps(inputForInvoker)
    )

    responseJson = json.load(response["Payload"])

    print(responseJson)
```