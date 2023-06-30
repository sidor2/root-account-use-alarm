#!/usr/bin/env python3
import os

import aws_cdk as cdk

from root_account_use_alarm.root_account_use_alarm_stack import RootAccountUseAlarmStack


app = cdk.App()
RootAccountUseAlarmStack(app, "RootAccountUseAlarmWithCloudTrailStack",
    with_cloudtrail=True,
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

RootAccountUseAlarmStack(app, "RootAccountUseAlarmStack",
    with_cloudtrail=False,
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
