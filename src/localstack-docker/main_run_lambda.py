import time
import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

ENDPOINT_URL = os.getenv("ENDPOINT_URL", "http://localhost:4566")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
BUCKET_NAME = os.getenv("BUCKET_NAME", "test-bucket")

def main():
    print(f"Connecting to LocalStack at {ENDPOINT_URL}...")
    
    lambda_client = boto3.client('lambda', endpoint_url=ENDPOINT_URL, region_name=AWS_REGION)
    
    payload = {
        "bucket_name": BUCKET_NAME,
        "key": "hello.txt",
        "body": "Hello from Lambda!"
    }
    
    print(f"Invoking Lambda function 'UploadToS3'...")
    response = lambda_client.invoke(
        FunctionName="UploadToS3",
        Payload=json.dumps(payload)
    )
    
    response_payload = json.loads(response['Payload'].read())
    print(f"Lambda response: {response_payload}")
    
    time.sleep(1)
    
    print("Verifying S3 upload...")
    s3 = boto3.client('s3', endpoint_url=ENDPOINT_URL, region_name=AWS_REGION)
    response = s3.get_object(Bucket=BUCKET_NAME, Key="hello.txt")
    content = response['Body'].read().decode('utf-8')
    print(f"Content from S3: {content}")

if __name__ == "__main__":
    main()
