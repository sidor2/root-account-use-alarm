
# Welcome to the Root Account Use Alarm CDK Python project!

1. RootAccountUseAlarm deploys an EventsBridge alarm.
- Use if you already have a CloudTrail enabled that you want to use

2. RootAccountUseAlarmWithCloudTrailStack also creates a CloudTrail trail

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

Deploy one of the stacks, with or without CloudTrail trail. Pass an email address that will be used for notifications.

```
$ cdk deploy RootAccountUseAlarmWithCloudTrailStack --parameters email=<email>  --profile <profile>
```

or

```
$ cdk deploy RootAccountUseAlarmStack --parameters email=<email>  --profile <profile>
```
