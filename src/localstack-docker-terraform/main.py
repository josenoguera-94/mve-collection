import os
import boto3
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Configuration from environment variables
ENDPOINT_URL = os.getenv("ENDPOINT_URL", "http://localhost:4566")
BUCKET_NAME = os.getenv("BUCKET_NAME", "file-uploads-bucket")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME", "file-logs")

# Initialize AWS clients
s3_client = boto3.client(
    's3',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

def upload_sample_files():
    """Upload sample files to S3 bucket."""
    print(f"\n{'='*60}")
    print("Uploading Sample Files to S3")
    print(f"{'='*60}\n")
    
    # Sample files to upload
    sample_files = [
        ("document.pdf", b"Sample PDF content", "application/pdf"),
        ("image.jpg", b"Sample image data", "image/jpeg"),
        ("archive.zip", b"Sample ZIP archive", "application/zip"),
        ("data.json", b'{"key": "value"}', "application/json")
    ]
    
    for filename, content, content_type in sample_files:
        try:
            s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=filename,
                Body=content,
                ContentType=content_type
            )
            print(f"✓ Uploaded: {filename} ({len(content)} bytes)")
        except Exception as e:
            print(f"✗ Error uploading {filename}: {str(e)}")
    
    print(f"\n{'='*60}")
    print("Waiting for Lambda to process files...")
    print(f"{'='*60}\n")
    
    # Wait for Lambda to process
    time.sleep(3)

def view_dynamodb_logs():
    """View logs from DynamoDB table."""
    print(f"\n{'='*60}")
    print("File Logs from DynamoDB")
    print(f"{'='*60}\n")
    
    try:
        table = dynamodb.Table(DYNAMODB_TABLE_NAME)
        response = table.scan()
        
        items = response.get('Items', [])
        
        if not items:
            print("No logs found in DynamoDB table.")
            return
        
        # Sort by timestamp
        items.sort(key=lambda x: x.get('upload_timestamp', ''), reverse=True)
        
        for item in items:
            print(f"File ID: {item.get('file_id')}")
            print(f"  Name: {item.get('file_name')}")
            print(f"  Size: {item.get('file_size')} bytes")
            print(f"  Type: {item.get('content_type')}")
            print(f"  Uploaded: {item.get('upload_timestamp')}")
            print()
    
    except Exception as e:
        print(f"Error reading from DynamoDB: {str(e)}")

def main():
    """Main demonstration script."""
    print("\n" + "="*60)
    print("LocalStack + Terraform Demo")
    print("S3 → Lambda → DynamoDB Pipeline")
    print("="*60)
    
    # Upload sample files
    upload_sample_files()
    
    # View logs from DynamoDB
    view_dynamodb_logs()
    
    print("="*60)
    print("Demo completed successfully!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
