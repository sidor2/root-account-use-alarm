import aws_cdk as core
import aws_cdk.assertions as assertions

from root_account_use_alarm.root_account_use_alarm_stack import RootAccountUseAlarmStack

# example tests. To run these tests, uncomment this file along with the example
# resource in root_account_use_alarm/root_account_use_alarm_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RootAccountUseAlarmStack(app, "root-account-use-alarm")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
