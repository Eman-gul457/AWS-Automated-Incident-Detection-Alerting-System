def lambda_handler(event, context):
    print("DevOps monitoring test started")
    raise Exception("Intentional error for CloudWatch monitoring")
