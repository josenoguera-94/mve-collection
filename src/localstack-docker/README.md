# LocalStack + Lambda + S3 Example

Minimal viable example to work with AWS services locally using LocalStack, Docker Compose, and Python. This example demonstrates how to create and deploy a Lambda function that uploads objects to S3.

## Project Structure

```
localstack-docker/
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── .env
├── deploy.py
├── lambda_s3_uploader.py
├── main_create_lambda.py
├── main_run_lambda.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (optional, for dev container setup)

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder
2. Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Type and select: **Dev Containers: Reopen in Container**
4. Wait for the container to build and dependencies to install

### Step 2: Start LocalStack Container

Inside the dev container terminal:

```bash
docker compose up -d
```

Verify it's running:

```bash
docker ps
```

### Step 3: Create Lambda Function and S3 Bucket

Run the creation script:

```bash
python main_create_lambda.py
```

You should see output like:

```
Connecting to LocalStack at http://localhost:4566...
Creating bucket 'test-bucket'...
Creating UploadToS3.zip...
Lambda function 'UploadToS3' deployed successfully!
You can now verify the function exists using AWS CLI.
```

### Step 4: Verify Lambda Function Exists

The dev container includes AWS CLI pre-installed. First, configure AWS credentials (LocalStack accepts any dummy values):

```bash
aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set region us-east-1
aws configure set output json
```

Then verify the Lambda function was created:

```bash
aws --endpoint-url=http://localhost:4566 lambda list-functions
```

Or get details about the specific function:

```bash
aws --endpoint-url=http://localhost:4566 lambda get-function --function-name UploadToS3
```

You should see the function details including its state, runtime, and handler.

**Alternative: Using Python Script**

If you prefer, you can verify using Python:

```python
import boto3
import os
from dotenv import load_dotenv

load_dotenv()
lambda_client = boto3.client('lambda', 
    endpoint_url=os.getenv("ENDPOINT_URL", "http://localhost:4566"),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"))

response = lambda_client.list_functions()
for func in response['Functions']:
    print(f"Function: {func['FunctionName']}, Runtime: {func['Runtime']}, State: {func['State']}")
```

### Step 5: Run Lambda Function

Now execute the Lambda function:

```bash
python main_run_lambda.py
```

You should see output like:

```
Connecting to LocalStack at http://localhost:4566...
Invoking Lambda function 'UploadToS3'...
Lambda response: {'statusCode': 200, 'body': 'Successfully uploaded hello.txt to test-bucket'}
Verifying S3 upload...
Content from S3: Hello from Lambda!
```

### Step 6: Verify S3 Object Using AWS CLI

You can also verify the S3 object was created using AWS CLI:

**List objects in the bucket:**

```bash
aws --endpoint-url=http://localhost:4566 s3 ls s3://test-bucket/
```

You should see `hello.txt` in the output.

**Read the object content:**

```bash
aws --endpoint-url=http://localhost:4566 s3 cp s3://test-bucket/hello.txt -
```

This will display the content: `Hello from Lambda!`

**Get object metadata:**

```bash
aws --endpoint-url=http://localhost:4566 s3api head-object --bucket test-bucket --key hello.txt
```

This shows metadata like size, last modified date, etc.

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Python Dependencies

```bash
pip3 install uv && uv sync
```

### Step 2: Start LocalStack Container

```bash
docker compose up -d
```

### Step 3: Create Lambda Function

```bash
python main_create_lambda.py
```

### Step 4: Verify Lambda Function

If you don't have AWS CLI installed locally, install it:

```bash
pip install awscli
```

Configure AWS credentials:

```bash
aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set region us-east-1
aws configure set output json
```

Then verify the Lambda function:

```bash
aws --endpoint-url=http://localhost:4566 lambda list-functions
```

### Step 5: Run Lambda Function

```bash
python main_run_lambda.py
```

## Project Components

### LambdaDeployer (`deploy.py`)

Class for deploying Lambda functions to LocalStack:

- **Constructor**: Reads environment variables (`ENDPOINT_URL`, `AWS_DEFAULT_REGION`, `LAMBDA_INTERNAL_ENDPOINT`) and creates the Lambda client
- **`deploy(lambda_file_path, dependencies, function_name)`**: Deploys a Lambda function
  - Creates a zip file with the function and its dependencies
  - Deletes any existing function with the same name
  - Creates the new Lambda function
  - Cleans up temporary files
- **Private methods**: `_create_zip()`, `_delete_lambda()`, `_remove_zip()` handle internal operations

### Lambda Function (`lambda_s3_uploader.py`)

Simple Lambda function that uploads objects to S3:

- **`lambda_handler(event, context)`**: Main entry point for the Lambda function
  - Receives `bucket_name`, `key`, and `body` in the event
  - Uses boto3 to upload the object to S3
  - Returns a success response

This is a standalone function with no inheritance or dependencies on custom classes.

### Main Scripts

**`main_create_lambda.py`**: 
- Creates the S3 bucket using boto3 (if it doesn't exist)
- Uses `LambdaDeployer` to deploy the Lambda function to LocalStack

**`main_run_lambda.py`**:
- Uses boto3 to invoke the Lambda function with a payload
- Verifies the file was uploaded to S3 using boto3 directly

## Environment Variables

The `.env` file contains:

```
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_DEFAULT_REGION=us-east-1
ENDPOINT_URL=http://localhost:4566
LAMBDA_INTERNAL_ENDPOINT=http://localstack:4566
BUCKET_NAME=test-bucket
```

## Useful Commands

### Docker Commands

```bash
# Start containers
docker compose up -d

# Stop containers
docker compose down

# Stop and remove volumes (delete all data)
docker compose down -v

# View logs
docker compose logs -f

# View only LocalStack logs
docker compose logs -f localstack
```

## Troubleshooting

### Port Already in Use

If port 4566 is already in use, modify the `docker-compose.yml` ports section:

```yaml
ports:
  - "4567:4566"
```

Then update `ENDPOINT_URL` in `.env`:

```
ENDPOINT_URL=http://localhost:4567
```

And restart:

```bash
docker compose down
docker compose up -d
```

### Connection Refused

Make sure the LocalStack container is running:

```bash
docker ps
```

Check the logs for errors:

```bash
docker compose logs localstack
```

### Module Not Found

If you get import errors, install dependencies:

```bash
pip3 install uv && uv sync
```

## Clean Up

To completely remove everything:

```bash
# Stop and remove containers and volumes
docker compose down -v

# Remove the LocalStack image (optional)
docker rmi localstack/localstack
```

## Next Steps

- Add more Lambda functions for different operations
- Implement API Gateway integration
- Add DynamoDB examples
- Implement SNS/SQS messaging patterns
- Add unit tests for Lambda functions

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
