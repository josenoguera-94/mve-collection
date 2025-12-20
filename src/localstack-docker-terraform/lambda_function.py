import json
import boto3
import os
from datetime import datetime
from urllib.parse import unquote_plus

# Initialize AWS clients
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Get DynamoDB table name from environment variable
table_name = os.environ.get('DYNAMODB_TABLE', 'file-logs')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Lambda function triggered by S3 upload events.
    Extracts file metadata and logs it to DynamoDB.
    
    Args:
        event: S3 event data
        context: Lambda context
    """
    try:
        # Get S3 event details
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            file_key = unquote_plus(record['s3']['object']['key'])
            file_size = record['s3']['object']['size']
            
            # Get file metadata from S3
            response = s3_client.head_object(Bucket=bucket_name, Key=file_key)
            
            # Prepare log entry
            timestamp = datetime.utcnow().isoformat()
            log_entry = {
                'file_id': f"{bucket_name}/{file_key}",
                'file_name': file_key,
                'file_size': file_size,
                'bucket_name': bucket_name,
                'upload_timestamp': timestamp,
                'content_type': response.get('ContentType', 'unknown')
            }
            
            # Save to DynamoDB
            table.put_item(Item=log_entry)
            
            print(f"Logged file: {file_key} ({file_size} bytes) at {timestamp}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('File metadata logged successfully')
        }
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
