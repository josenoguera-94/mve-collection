import zipfile
import io
import os

def create_lambda_zip(file_path):
    """Create a ZIP file containing the lambda function."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.write(file_path, arcname=os.path.basename(file_path))
    return buf.getvalue()

def get_boto_config():
    """Returns standard boto3 configuration for LocalStack."""
    return {
        "endpoint_url": os.getenv("LOCALSTACK_ENDPOINT", "http://localhost:4566"),
        "region_name": os.getenv("AWS_REGION", "us-east-1"),
        "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID", "test"),
        "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY", "test")
    }
