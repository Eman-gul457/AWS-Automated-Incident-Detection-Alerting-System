🔔 AWS Automated Incident Detection & Alerting System
---
📌 About This Project:
---
In modern systems, applications can fail at any time.
If no one knows about the failure, the problem becomes bigger.
This project automatically detects errors in AWS, analyzes how serious they are, stores them, and sends an email alert — without any human involvement.

👉 Goal:
---
Make sure that whenever something breaks, we know immediately.

----
🧠 What Problem Does This Solve?
---
Before this system:
---
-Errors happen silently ❌
-Engineers manually check logs ❌
-Incidents are noticed late ❌

After this system:
---
•Errors are detected automatically ✅
•Incidents are saved and tracked ✅
•Alerts are sent instantly via email ✅

---

🏗️ High-Level Architecture
🔁 Flow of the System
---
<img width="1536" height="1024" alt="Architecture of Project" src="https://github.com/user-attachments/assets/22cfc1b9-1ce8-4b3f-b6c1-e4d7ffed9008" />

---
## 🧰 Tech Stack

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![Lambda](https://img.shields.io/badge/AWS-Lambda-orange?logo=awslambda)
![CloudWatch](https://img.shields.io/badge/AWS-CloudWatch-orange?logo=amazoncloudwatch)
![EventBridge](https://img.shields.io/badge/AWS-EventBridge-orange?logo=amazonaws)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue?logo=amazondynamodb)
![SNS](https://img.shields.io/badge/AWS-SNS-red?logo=amazonsns)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

---
🛠️ STEP-BY-STEP IMPLEMENTATION:
---
Below is exactly how this project was built, step by step.
---

STEP 1 — Create IAM Role for Lambda
---
Why?
---
AWS Lambda needs permission to:
•Write logs
•Access DynamoDB
•Send SNS emails

Actions:
---
•Created IAM Role
•Attached policies:
  •CloudWatchLogs
  •DynamoDB access
  •SNS publish

---
<img width="1351" height="457" alt="sns-permission" src="https://github.com/user-attachments/assets/63d72c04-03f3-4c20-9c1b-8d3c07202366" />

---
STEP 2 — Create DynamoDB Table
---
Why?
---
We need to store incidents permanently.

Table Details:
---
  •Table name: devops-incidents
  •Partition key: incident_id
•Each record stores:
  •Incident ID
  •Time
  •Severity
  •Summary
  •Recommendation

---
<img width="1235" height="467" alt="dynamodb-table-created" src="https://github.com/user-attachments/assets/dd31a27b-840f-49d5-996e-8079c5f6de20" />

---
STEP 3 — Create SNS Topic & Email Subscription
---
Why?
---
Engineers must receive alerts immediately.

Actions:
---
•Created SNS topic
•Subscribed email address
•Confirmed email subscription
•Granted publish permission to Lambda

--
<img width="967" height="436" alt="sns-email-alert-redacted_dot_app" src="https://github.com/user-attachments/assets/0647f190-07fc-4d87-8fce5289650b966e" />

---
STEP 4 — Create Error Generator Lambda (Testing)
---
Purpose:
---
To intentionally create an error so monitoring can be tested.

Lambda Function:
---
```bash
def lambda_handler(event, context):
    print("DevOps monitoring test started")
    raise Exception("Intentional error for CloudWatch monitoring")
```
What This Does:
---
•Runs
•Fails intentionally
•Sends error to CloudWatch

---
<img width="959" height="491" alt="lambda-error-code" src="https://github.com/user-attachments/assets/48812acd-66d6-48f1-8dad-d77b40d059a2" />

---
<img width="951" height="260" alt="lambda-test-error" src="https://github.com/user-attachments/assets/6a7f857d-e0b3-4a1e-9b37-82aadbeea825" />

---
STEP 5 — CloudWatch Logs & Metrics
---
Why?
---
CloudWatch captures:
•Error logs
•Failure metrics
•Execution details
This is how AWS detects something went wrong.

---
<img width="1358" height="569" alt="cloudwatch-error-logs" src="https://github.com/user-attachments/assets/ad8fbd18-5e81-45f2-b46c-d942b7bebce3" />

---
<img width="1349" height="556" alt="lambda-metrics" src="https://github.com/user-attachments/assets/27144c27-6056-4129-8a37-07fd9ab392ae" />

---
STEP 6 — Create EventBridge Rule
---
Why?
---
EventBridge listens for Lambda failure events and triggers automation.

Rule:
---
•Source: AWS Lambda
•Event type: Function failure
•Target: Incident Handler Lambda

---
<img width="1334" height="485" alt="eventbridge-rule" src="https://github.com/user-attachments/assets/9d73d6b9-95a3-42a3-914e-0f6f68839108" />

---

STEP 7 — Incident Handler Lambda (Core Logic)
---
This Lambda does everything automatically.

Responsibilities:
---
1.Receive error event
2.Analyze severity (AI-style logic)
3.Save incident to DynamoDB
4.Send email alert using SNS

---

STEP 8 — AI-Style Incident Analysis
---
What “AI-style” Means Here:
---
•Rule-based decision making
•Severity classification
•Action recommendations
Example logic:
```bash
if "Timeout" in error_type:
    severity = "HIGH"
```
This is commonly used in real monitoring systems.

---
<img width="1350" height="516" alt="ai-analysis-logs" src="https://github.com/user-attachments/assets/ef87628b-cac3-4024-91b7-a0fe03f5857b" />

---
STEP 9 — Save Incident to DynamoDB
---
Each incident is saved with:
•Unique ID
•Timestamp
•Severity
•Summary
•Recommendation

---
<img width="1361" height="571" alt="dynamodb-ai-fields" src="https://github.com/user-attachments/assets/ff6ff3da-219c-482d-9a2b-b6a7281edc72" />

---
STEP 10 — Send SNS Email Alert
---
When an incident happens:
•SNS sends an email
•Email includes:
  •Incident ID
  •Severity
  •Summary
  •Recommendation

---
<img width="1353" height="565" alt="ai-alert-email-redacted_dot_app" src="https://github.com/user-attachments/assets/f3a33097-2ee4-44ed-afdb-f5b1005fa6a3" />

---
✅ Final Outcome
---
•Errors detected automatically
•Incidents analyzed intelligently
•Data stored securely
•Alerts delivered instantly
•No manual monitoring required

----
🚀 What This Project Demonstrates
---
•DevOps mindset
•Incident response automation
•AWS monitoring skills
•Event-driven architecture
•Cloud troubleshooting
•Real-world production thinking

---
