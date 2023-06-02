from aws_cdk import (
    Stack,
    aws_events as events,
    aws_events_targets as event_target,
    aws_sns as _sns,
    aws_sns_subscriptions as sns_sub,
    CfnParameter
)
from constructs import Construct


# Before you begin, make sure that your AWS CloudTrail Management read/write events are set to All or Write-only
# for EventBridge events to trigger the log-in event notification.

class RootAccountUseAlarmStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define an event rule
        rule = events.Rule(
            self,
            "root-account-use-alarm",
            rule_name="root-account-use-alarm"
        )

        # Define the event pattern to look for
        rule.add_event_pattern(
            detail_type=["AWS Console Sign In via CloudTrail"],
            detail={
                "userIdentity": {
                    "type": ["Root"]
                }
            }
        )

        # create an SNS topic
        alarm_topic = _sns.Topic(
            self,
            "root-alarm-topic",
            display_name="root-alarm-topic"
        )

        # parameter for email subscription
        email_address = CfnParameter(
            self,
            "emailparam",
            allowed_pattern="^[\\x20-\\x45]?[\\w-\\+]+(\\.[\\w]+)*@[\\w-]+(\\.[\\w]+)*(\\.[a-z]{2,})$"
        )

        # create the subscription to the root-alarm-topic
        alarm_topic_sub=sns_sub.EmailSubscription(email_address.value_as_string)
        alarm_topic.add_subscription(alarm_topic_sub)

        # add the SNS topic as a target to the event rule
        rule_target=event_target.SnsTopic(
            alarm_topic,
            message=events.RuleTargetInput.from_text(
                f"Root account login detected for account {events.EventField.from_path('$.detail.userIdentity.accountId')}"
            )
        )
        rule.add_target(rule_target)
