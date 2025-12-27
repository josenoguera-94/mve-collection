import os
import boto3
import zipfile
from dotenv import load_dotenv

load_dotenv()

ENDPOINT_URL = os.getenv("ENDPOINT_URL", "http://localhost:4566")
REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

def create_zip(zip_path, folder_path):
    with zipfile.ZipFile(zip_path, 'w') as z:
        for root, _, files in os.walk(folder_path):
            for file in files:
                z.write(os.path.join(root, file), file)

def main():
    lambda_client = boto3.client('lambda', endpoint_url=ENDPOINT_URL, region_name=REGION)
    zip_path = "lambda.zip"
    create_zip(zip_path, "add_user_lambda")

    with open(zip_path, 'rb') as f:
        zipped_code = f.read()

    try:
        lambda_client.delete_function(FunctionName="AddUserFunction")
    except: pass

    lambda_client.create_function(
        FunctionName="AddUserFunction",
        Runtime='python3.9',
        Role="arn:aws:iam::000000000000:role/lambda-role",
        Handler="lambda_handler.lambda_handler",
        Code={'ZipFile': zipped_code},
        Environment={'Variables': {'AWS_ENDPOINT_URL': 'http://172.17.0.1:4566'}}
    )
    print("Lambda 'AddUserFunction' deployed!")
    os.remove(zip_path)

if __name__ == "__main__":
    main()
