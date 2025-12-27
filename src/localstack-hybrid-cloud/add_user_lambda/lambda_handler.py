import os
import boto3
import random
import string
from models import User, get_session

def lambda_handler(event, context):
    client = boto3.client('secretsmanager', endpoint_url=os.getenv("AWS_ENDPOINT_URL"))
    response = client.get_secret_value(SecretId='postgres-connection-uri')
    db_uri = response['SecretString']

    session = get_session(db_uri)
    name = "".join(random.choices(string.ascii_letters, k=8))
    user = User(name=name, email=f"{name}@example.com")
    
    session.add(user)
    session.commit()
    print(f"User {name} created successfully!")
    return {"status": "success", "user": name}
