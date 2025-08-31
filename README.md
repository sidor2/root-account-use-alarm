# AWS CDK Root Account Use Alarm

A serverless AWS CDK stack that sets up an Amazon EventBridge alarm to detect root account logins and sends notifications via Amazon SNS, with optional CloudTrail integration for monitoring.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org)
[![AWS CDK](https://img.shields.io/badge/AWS_CDK-v2-orange)](https://aws.amazon.com/cdk/)

## Overview

This project provides two CDK stack variations to monitor root account usage:
- **`RootAccountUseAlarmStack`**: Deploys an EventBridge alarm using an existing CloudTrail trail.
- **`RootAccountUseAlarmWithCloudTrailStack`**: Includes a dedicated CloudTrail trail for root account management events alongside the alarm.

Notifications are sent via Amazon SNS when root account logins are detected, enhancing account security.

![Thumbnail - AWS CDK Root Account Use Alarm](./thumbnail.png "AWS CDK Root Account Use Alarm Diagram")

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Deployment](#deployment)
- [Cleanup](#cleanup)
- [Additional Resources](#additional-resources)

## Features
- **Root Account Monitoring**: Detects root account logins using Amazon EventBridge.
- **Flexible Deployment**: Supports existing CloudTrail trails or creates a new one.
- **Notification System**: Sends alerts via Amazon SNS.
- **CDK-Based**: Infrastructure defined and deployed using AWS Cloud Development Kit (CDK).
- **Security Focused**: Helps enforce best practices by alerting on unauthorized root usage.

## Prerequisites
- **AWS CLI**: Installed and configured with appropriate credentials.
- **Node.js**: Required for AWS CDK (version 14 or higher recommended).
- **Python**: Version 3.8 or higher (for virtual environment setup).
- **AWS Account**: With permissions to create EventBridge rules, CloudTrail trails, and SNS topics.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/repo.git
   cd aws-cdk-root-account-use-alarm
   ```
2. Create and activate a virtual environment:
   - **MacOS/Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows**:
     ```bash
     py -3 -m venv .venv
     .venv\Scripts\activate.bat
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Deployment
1. Synthesize the CloudFormation template:
   ```bash
   cdk synth
   ```
2. Deploy one of the following stacks based on your needs:
   - **Option 1: With CloudTrail Trail** (if no existing trail or want a dedicated one):
     ```bash
     cdk deploy RootAccountUseAlarmWithCloudTrailStack --parameters email=<your-email> --profile <your-profile>
     ```
   - **Option 2: With Existing Trail**:
     ```bash
     cdk deploy RootAccountUseAlarmStack --parameters email=<your-email> --profile <your-profile>
     ```
   - **Notes**:
     - Replace `<your-email>` with the email address to receive SNS notifications.
     - Replace `<your-profile>` with your AWS CLI profile name.

## Cleanup
To remove the stack and its resources from your AWS account:
```bash
cdk destroy --profile <your-profile>
```
- Replace `<your-profile>` with your AWS CLI profile name.
- This command deletes all resources created by the deployed stack.

## Additional Resources
- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [AWS CloudTrail Documentation](https://aws.amazon.com/cloudtrail/)
- [Amazon SNS Documentation](https://aws.amazon.com/sns/)
- [Amazon EventBridge Documentation](https://aws.amazon.com/eventbridge/)