from aws_cdk import (
    Stack,
    aws_cloudtrail as ct,
    aws_s3 as _s3,
    aws_sns as _sns,
    aws_events as events,
    aws_events_targets as event_target,
    aws_sns_subscriptions as sns_sub,
    CfnParameter
)
from constructs import Construct


class RootAccountUseAlarmCloudTrailStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create s3 bucket with BPA enabled
        ct_bucket=_s3.Bucket(
            self,
            "ct_bucket",
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            encryption=_s3.BucketEncryption.UNENCRYPTED
        )

        # Define a trail
        trail = ct.Trail(
            self,
            "root_account_use_alarm_with_cloudtrail-trail",
            bucket=ct_bucket,
            send_to_cloud_watch_logs=False,
            enable_file_validation=False,
            include_global_service_events=False,
            is_multi_region_trail=False,
            is_organization_trail=False, # organizational trail is failing; https://github.com/aws/aws-cdk/issues/22267
            management_events=ct.ReadWriteType.WRITE_ONLY
        )

        event_rule=ct.Trail.on_event(
            self,
            "root-account-use-alarm-cloudtrail",
            rule_name="root-account-use-alarm-cloudtrail",
        )

        event_rule.add_event_pattern(
            detail_type=["AWS Console Sign In via CloudTrail"],
            detail={
                "userIdentity": {
                    "type": ["Root"]
                }
            }
        )

        # parameter for email subscription
        email_address = CfnParameter(
            self,
            "emailparam",
            allowed_pattern="^[\\x20-\\x45]?[\\w-\\+]+(\\.[\\w]+)*@[\\w-]+(\\.[\\w]+)*(\\.[a-z]{2,})$"
        )

        # create an SNS topic
        alarm_topic = _sns.Topic(
            self,
            "root-alarm-topic",
            display_name="root-alarm-topic"
        )

        # create the subscription to the root-alarm-topic
        alarm_topic_sub = sns_sub.EmailSubscription(email_address.value_as_string)
        alarm_topic.add_subscription(alarm_topic_sub)

        # add the SNS topic as a target to the event rule
        event_rule_target = event_target.SnsTopic(
            alarm_topic,
            message=events.RuleTargetInput.from_text(
                f"Root account login detected for account {events.EventField.from_path('$.detail.userIdentity.accountId')}"
            )
        )

        event_rule.add_target(event_rule_target)