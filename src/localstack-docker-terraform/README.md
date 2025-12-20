# LocalStack + Terraform Example

Minimal viable example to work with LocalStack using Terraform for infrastructure provisioning. This example demonstrates how to create a complete AWS-like environment locally with S3, Lambda, and DynamoDB, all managed through Terraform.

## What This Example Does

This example creates a file processing pipeline:

1. **S3 Bucket**: Receives uploaded files (PDF, images, ZIP, etc.)
2. **Lambda Function**: Automatically triggered when a file is uploaded to S3
3. **DynamoDB Table**: Stores logs with file metadata (name, size, timestamp)

All infrastructure is provisioned using **Terraform** and runs locally on **LocalStack**.

## Project Structure

```
localstack-docker-terraform/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── docker-compose.yml
├── .env
├── main.tf                    # Terraform configuration
├── lambda_function.py         # Lambda function code
├── package_lambda.py          # Script to package Lambda
├── main.py                    # Demo script
├── pyproject.toml
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (optional, for dev container setup)
- Terraform installed (automatically included in Dev Container)

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder
2. Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Type and select: **Dev Containers: Reopen in Container**
4. Wait for the container to build and dependencies to install

The Dev Container includes:
- Python 3.12
- Terraform
- AWS CLI
- Docker support
- All Python dependencies

### Step 2: Start LocalStack

```bash
docker compose up -d
```

Wait a few seconds for LocalStack to be ready:

```bash
docker compose logs -f
```

You should see: `Ready.`

### Step 3: Package the Lambda Function

```bash
python package_lambda.py
```

This creates `lambda_function.zip` required by Terraform.

### Step 4: Deploy Infrastructure with Terraform

Initialize Terraform:

```bash
terraform init
```

Apply the Terraform configuration:

```bash
terraform apply
```

Type `yes` when prompted. Terraform will create:
- S3 bucket (`file-uploads-bucket`)
- DynamoDB table (`file-logs`)
- Lambda function (`s3-file-processor`)
- IAM roles and policies
- S3 event notification

You should see output like:

```
Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

bucket_name = "file-uploads-bucket"
dynamodb_table_name = "file-logs"
lambda_function_name = "s3-file-processor"
```

### Step 5: Run the Demo

```bash
python main.py
```

You should see output like:

```
============================================================
LocalStack + Terraform Demo
S3 → Lambda → DynamoDB Pipeline
============================================================

============================================================
Uploading Sample Files to S3
============================================================

✓ Uploaded: document.pdf (18 bytes)
✓ Uploaded: image.jpg (17 bytes)
✓ Uploaded: archive.zip (18 bytes)
✓ Uploaded: data.json (16 bytes)

============================================================
Waiting for Lambda to process files...
============================================================

============================================================
File Logs from DynamoDB
============================================================

File ID: file-uploads-bucket/data.json
  Name: data.json
  Size: 16 bytes
  Type: application/json
  Uploaded: 2025-12-16T08:36:45.123456

File ID: file-uploads-bucket/archive.zip
  Name: archive.zip
  Size: 18 bytes
  Type: application/zip
  Uploaded: 2025-12-16T08:36:45.098765

...

============================================================
Demo completed successfully!
============================================================
```

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Dependencies

Install Terraform:

```bash
# On Ubuntu/Debian
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

Install Python dependencies:

```bash
pip3 install uv && uv sync
```

### Step 2: Start LocalStack

```bash
docker compose up -d
```

### Step 3: Package Lambda and Deploy with Terraform

```bash
python package_lambda.py
terraform init
terraform apply
```

### Step 4: Run the Demo

```bash
python main.py
```

## Project Components

### Terraform Configuration (`main.tf`)

Defines the complete infrastructure:

- **AWS Provider**: Configured to use LocalStack endpoints
- **S3 Bucket**: `file-uploads-bucket` for file storage
- **DynamoDB Table**: `file-logs` with `file_id` as hash key
- **IAM Role**: For Lambda execution with necessary permissions
- **Lambda Function**: Processes S3 events and logs to DynamoDB
- **S3 Event Notification**: Triggers Lambda on file uploads
- **Outputs**: Displays created resource names

### Lambda Function (`lambda_function.py`)

Triggered automatically when files are uploaded to S3:

- Extracts file metadata (name, size, content type)
- Generates timestamp
- Logs information to DynamoDB table

### Demo Script (`main.py`)

Demonstrates the complete workflow:

- Uploads sample files to S3 (PDF, JPG, ZIP, JSON)
- Waits for Lambda processing
- Queries and displays logs from DynamoDB

### Package Script (`package_lambda.py`)

Creates the ZIP package required for Lambda deployment:

- Packages `lambda_function.py` into `lambda_function.zip`
- Required before running `terraform apply`

## Environment Variables

The `.env` file contains:

```
# AWS Credentials (for LocalStack)
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_DEFAULT_REGION=us-east-1

# LocalStack Configuration
ENDPOINT_URL=http://localhost:4566

# S3 Configuration
BUCKET_NAME=file-uploads-bucket

# DynamoDB Configuration
DYNAMODB_TABLE_NAME=file-logs
```

**Note**: LocalStack accepts any credentials in local development. The values `test/test` are standard placeholders.

## Useful Commands

### Docker Commands

```bash
# Start LocalStack
docker compose up -d

# Stop LocalStack
docker compose down

# View logs
docker compose logs -f

# Restart LocalStack
docker compose restart
```

### Terraform Commands

```bash
# Initialize Terraform
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy

# Show current state
terraform show

# List resources
terraform state list
```

### AWS CLI Commands (with LocalStack)

```bash
# List S3 buckets
aws --endpoint-url=http://localhost:4566 s3 ls

# List files in bucket
aws --endpoint-url=http://localhost:4566 s3 ls s3://file-uploads-bucket

# Scan DynamoDB table
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name file-logs

# List Lambda functions
aws --endpoint-url=http://localhost:4566 lambda list-functions
```

## How It Works

1. **Infrastructure Provisioning**: Terraform creates all AWS resources in LocalStack
2. **File Upload**: When a file is uploaded to S3, an event is generated
3. **Lambda Trigger**: S3 event notification triggers the Lambda function
4. **Metadata Extraction**: Lambda extracts file name, size, and timestamp
5. **Logging**: Lambda writes the metadata to DynamoDB
6. **Query**: You can query DynamoDB to see all file logs

## Troubleshooting

### Port Already in Use

If port 4566 is already in use, modify the `docker-compose.yml`:

```yaml
ports:
  - "4567:4566"
```

And update `ENDPOINT_URL` in `.env` and `main.tf`.

### Terraform Apply Fails

Make sure LocalStack is running:

```bash
docker ps
```

You should see `localstack_terraform_local` container running.

### Lambda Not Triggering

Check Lambda logs:

```bash
aws --endpoint-url=http://localhost:4566 logs tail /aws/lambda/s3-file-processor --follow
```

### Lambda Package Not Found

Make sure to run `package_lambda.py` before `terraform apply`:

```bash
python package_lambda.py
```

## Clean Up

To completely remove everything:

```bash
# Destroy Terraform resources
terraform destroy

# Stop and remove containers
docker compose down -v

# Remove Lambda package
rm lambda_function.zip

# Remove Terraform state
rm -rf .terraform terraform.tfstate*
```

## Next Steps

- Add more Lambda functions for different file types
- Implement file validation and error handling
- Add SNS notifications for processing results
- Create API Gateway endpoints
- Add CloudWatch metrics and alarms
- Implement Step Functions for complex workflows

## Why Terraform + LocalStack?

- **Infrastructure as Code**: Version control your infrastructure
- **Local Development**: Test AWS services without cloud costs
- **Reproducible**: Same infrastructure every time
- **Fast Iteration**: No waiting for cloud provisioning
- **Learning**: Practice Terraform and AWS services safely

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
