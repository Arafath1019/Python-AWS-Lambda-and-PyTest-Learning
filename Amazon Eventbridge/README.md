# Amazon EventBridge

#### What is amazon EventBridge?
Amazon EventBridge is a serverless event bus that makes it easier to build event-driven applications at scale using events generated from your applications, integrated Software-as-a-Service (SaaS) applications, and AWS services.

<img src="images/1.png" alt="Networking 1" height="300" width="700">

<img src="images/2.png" alt="Networking 1" height="300" width="700">

#### What is an Event?
1. Record of action
2. Represented as a JSON object
3. Meta data about the event
4. Data from the event

#### Comparing EventBridge to Amazon SQS
Event Bridge:
    - Processed one at a time
    - Can match multiple rules and be sent to multiple targets

SQS:
    - Events processed in batches
    - Events no longer available after successful processing

#### AWS Step Functions
AWS Step Functions is a visual workflow service that helps developers use AWS services to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning (ML) pipelines.

#### Integrating Amazon EventBridge events with AWS Step Functions
1. Create a state machine in Step Functions
2. Create a target event bus in Amazon EventBridge
3. Create a rule for the targeted event bus
4. Sent an event from the event bus

Reference:
1. EventBridge to Step Functions: https://serverlessland.com/patterns/eventbridge-sfn
2. Step Functions to EventBridge: https://serverlessland.com/patterns/sfn-eventbridge