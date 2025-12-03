import os
import boto3
from dotenv import load_dotenv
from deploy import LambdaDeployer

load_dotenv()

ENDPOINT_URL = os.getenv("ENDPOINT_URL", "http://localhost:4566")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
BUCKET_NAME = os.getenv("BUCKET_NAME", "test-bucket")

def main():
    print(f"Connecting to LocalStack at {ENDPOINT_URL}...")
    
    s3 = boto3.client('s3', endpoint_url=ENDPOINT_URL, region_name=AWS_REGION)
    
    # Try to create bucket
    try:
        print(f"Creating bucket '{BUCKET_NAME}'...")
        s3.create_bucket(Bucket=BUCKET_NAME)
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket '{BUCKET_NAME}' already exists.")
    
    # Deploy Lambda function
    deployer = LambdaDeployer()
    deployer.deploy(
        lambda_file_path="lambda_s3_uploader.py",
        function_name="UploadToS3"
    )
    
    print("You can now verify the function exists using AWS CLI.")

if __name__ == "__main__":
    main()
