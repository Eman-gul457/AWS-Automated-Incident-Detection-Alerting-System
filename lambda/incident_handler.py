import json
import uuid
import boto3
from datetime import datetime

# DynamoDB setup
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("devops-incidents")

# SNS setup
sns = boto3.client("sns")
SNS_TOPIC_ARN = "<your-sns-topic-arn>"

def ai_analyze_incident(event):
    detail = event.get("detail", {})
    error_type = detail.get("errorType", "UnknownError")

    if "Timeout" in error_type:
        return {
            "severity": "HIGH",
            "summary": "Lambda execution timed out",
            "recommendation": "Increase timeout or optimize function logic"
        }

    if "AccessDenied" in error_type:
        return {
            "severity": "HIGH",
            "summary": "Permission denied error",
            "recommendation": "Review IAM permissions"
        }

    return {
        "severity": "MEDIUM",
        "summary": "Unhandled Lambda failure",
        "recommendation": "Check CloudWatch logs for root cause"
    }

def lambda_handler(event, context):
    incident_id = str(uuid.uuid4())
    ai_result = ai_analyze_incident(event)

    item = {
        "incident_id": incident_id,
        "timestamp": datetime.utcnow().isoformat(),
        "source": event.get("source", "aws.lambda"),
        "detail_type": event.get("detail-type", "failure"),
        "ai_severity": ai_result["severity"],
        "ai_summary": ai_result["summary"],
        "ai_recommendation": ai_result["recommendation"]
    }

    # Save incident
    table.put_item(Item=item)

    # Send alert
    message = (
        f"Incident ID: {incident_id}\n"
        f"Severity: {ai_result['severity']}\n"
        f"Summary: {ai_result['summary']}\n"
        f"Recommendation: {ai_result['recommendation']}\n"
    )

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"DevOps Incident Alert ({ai_result['severity']})",
        Message=message
    )

    return {"status": "alert_sent", "incident_id": incident_id}
