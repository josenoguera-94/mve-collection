import os
import boto3
import json
from dotenv import load_dotenv
from add_user_lambda.models import User, get_session

load_dotenv()

def main():
    endpoint = os.getenv("ENDPOINT_URL", "http://localhost:4566")
    region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    lambda_client = boto3.client('lambda', endpoint_url=endpoint, region_name=region)

    print("Invoking Lambda...")
    response = lambda_client.invoke(FunctionName="AddUserFunction")
    result = json.loads(response['Payload'].read())
    print(f"Lambda Result: {result}")

    print("\nVerifying in Postgres...")
    db_uri = "postgresql://myuser:mypassword@localhost:5432/mydb"
    session = get_session(db_uri)
    last_user = session.query(User).order_by(User.id.desc()).first()
    print(f"Found in DB: {last_user.name} (Created at: {last_user.created_at})")

if __name__ == "__main__":
    main()
