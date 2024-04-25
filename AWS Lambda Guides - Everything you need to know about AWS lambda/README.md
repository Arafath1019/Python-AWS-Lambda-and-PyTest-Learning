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

## API Gateway to Lambda

<img src="images/3.png" alt="Networking 1" height="200" width="700">

TransactionProcessor Lambda Function:
```
import json

print("Loading function")

def lambda_handler(event, context):
    transactionId = event["queryStringParameters"]["transactionId"]
    transactionType = event["queryStringParameters"]["type"]
    transactionAmount = event["queryStringParameters"]["amount"]
    
    print("TransactionId", transactionId)
    print("TransactionType", transactionType)
    print("TransactionAmount", transactionAmount)
    
    transactionResponse = {}
    transactionResponse["transactionId"] = transactionId
    transactionResponse["type"] = transactionType
    transactionResponse["transactionAmount"] = transactionAmount
    transactionResponse["message"] = "Success"
    
    responseObject = {}
    responseObject["statusCode"] = 200
    responseObject["headers"] = {}
    responseObject["headers"]["content-type"] = "application/json"
    responseObject["body"] = json.dumps(transactionResponse)
    
    return responseObject
```

## Step Function with Lambda
<img src="images/4.png" alt="Networking 1" height="400" width="700">

ProcessPurchase Lambda Function:
```
from __future__ import print_function

import json
import urllib
import boto3
import datetime

print("Loading function...")

def lambda_handler(event, context):
    
    print("Received message from Step Functions: ")
    print(event)
    
    response = {}
    response['TransactionType'] = event['TransactionType']
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    response['Message'] = "Hello from lambda land inside the ProcessPurchase function"
    
    return response
```

* Create a IAM Policy for Step Function

Step Function Code:
```
{
  "Comment": "Transaction Processor State Machine",
  "StartAt": "ProcessTransaction",
  "States": {
    "ProcessTransaction": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.TransactionType",
          "StringEquals": "PURCHASE",
          "Next": "ProcessPurchase"
        },
        {
          "Variable": "$.TransactionType",
          "StringEquals": "REFUND",
          "Next": "ProcessRefund"
        }
      ]
    },
    "ProcessRefund": {
      "Type": "Task",
      "Resource": "arn",
      "End": true
    },
    "ProcessPurchase": {
      "Type": "Task",
      "Resource": "arn",
      "End": true
    }
  }
}
```

<img src="images/5.png" alt="Networking 1" height="250" width="700">