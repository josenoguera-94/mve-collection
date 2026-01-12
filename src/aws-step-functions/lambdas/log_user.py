import boto3
import os
from datetime import datetime

dynamodb = boto3.resource("dynamodb", endpoint_url=os.getenv("LOCALSTACK_ENDPOINT", "http://localhost:4566"))
table = dynamodb.Table(os.getenv("DYNAMODB_TABLE", "UserLogs"))

def handler(event, context):
    """Log user creation to DynamoDB."""
    username = event.get("username")
    email = event.get("email")
    
    table.put_item(Item={
        "username": username,
        "email": email,
        "created_at": datetime.now().isoformat()
    })
    return {"status": "Logged", "username": username}
