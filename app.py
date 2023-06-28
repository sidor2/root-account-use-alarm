#!/usr/bin/env python3
import os

import aws_cdk as cdk

from root_account_use_alarm.root_account_use_alarm_stack import RootAccountUseAlarmStack
from root_account_use_alarm_with_cloudtrail.root_account_use_alarm_with_cloudtrail_stack \
    import RootAccountUseAlarmCloudTrailStack
# from trail_only.trail_only import CloudTrailOnlyStack

app = cdk.App()
RootAccountUseAlarmStack(
    app,
    "RootAccountUseAlarmStack",
    with_ct=False,
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    )

# RootAccountUseAlarmCloudTrailStack(
#     app,
#     "RootAccountUseAlarmCloudTrailStack",
#     env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
# )

# CloudTrailOnlyStack(
#     app,
#     "CloudTrailOnlyStack",
#     env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
# )

app.synth()
