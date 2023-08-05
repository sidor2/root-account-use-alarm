# AWS CDK Root Account Use Alarm

This AWS CDK stack sets up an Amazon EventBridge alarm to detect root account logins and sends a notification through Amazon SNS when such logins are detected. There are two variations of the stack available:

`RootAccountUseAlarmStack`: This stack deploys an EventBridge alarm. Use this if you already have CloudTrail enabled and want to use an existing trail.

`RootAccountUseAlarmWithCloudTrailStack`: This stack also creates an AWS CloudTrail trail for management events related to the root account. Use this if you don't have an existing trail or want to create a dedicated trail for root account management events.

## Prerequisites

Before deploying this stack, you need the following prerequisites:

1. AWS CLI installed and configured with appropriate credentials.
2. Node.js installed, as the AWS CDK is built on Node.js.
3. Python 3 installed (for creating a virtual environment).

## Virtual Environment Setup

Create a virtual environment for the project inside the main directory. On macOS and Linux, use the following command:
```bash
python3 -m venv .venv
```

On Windows, use the following command:
```bash
py -3 -m venv .venv
```

Activate the virtual environment. On macOS and Linux, use the following command:
```bash
source .venv/bin/activate
```

On Windows, use the following command:
```bash
.venv\Scripts\activate.bat
```

## Install Dependencies
Install the dependencies for the project:
```bash
pip install -r requirements.txt
```

## CloudFormation Template Synthesis
After activating the virtual environment, synthesize the CloudFormation template for this code:
```bash
cdk synth
```

## Deployment Steps
Choose one of the following stacks to deploy, depending on whether you have an existing CloudTrail trail or want to create a new one:
Option 1: Deploying RootAccountUseAlarmWithCloudTrailStack (with CloudTrail trail)
```bash
cdk deploy RootAccountUseAlarmWithCloudTrailStack --parameters email=<email> --profile <profile>
```

Option 2: Deploying RootAccountUseAlarmStack (without CloudTrail trail)
```bash
cdk deploy RootAccountUseAlarmStack --parameters email=<email> --profile <profile>
```

## Clean Up
To remove the stack and its resources from your AWS account, use the following command:

```bash
cdk destroy --profile <profile>
```
This command will delete all the resources created by the stack.

## Additional Information

- AWS CDK documentation: https://docs.aws.amazon.com/cdk/latest/guide/home.html
- AWS CloudTrail documentation: https://aws.amazon.com/cloudtrail/
- Amazon SNS documentation: https://aws.amazon.com/sns/
- Amazon EventBridge documentation: https://aws.amazon.com/eventbridge/
