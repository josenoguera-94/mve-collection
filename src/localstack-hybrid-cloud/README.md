# LocalStack Hybrid Cloud Example

Minimal viable example to demonstrate a hybrid cloud scenario using LocalStack and an external PostgreSQL instance. This example shows how an AWS Lambda (simulated in LocalStack) can retrieve secrets from Secrets Manager and interact with a database outside the AWS environment.

## Project Structure

```
localstack-hybrid-cloud/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── add_user_lambda/          # Lambda function code
│   ├── lambda_handler.py
│   └── models.py
├── docker-compose.yml        # LocalStack + Postgres
├── .env
├── main.py                   # Run and verify script
├── main_create_lambda.py     # Deploy lambda script
├── main.tf                   # Infrastructure (Terraform)
├── pyproject.toml
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- Terraform installed
- VS Code with Dev Containers extension (optional)

## Deployment Steps

### Step 1: Start Infrastructure

```bash
docker compose up -d
```

Wait until services are ready.

### Step 2: Initialize Database and Secrets

```bash
terraform init
terraform apply -auto-approve
```

### Step 3: Deploy Lambda Function

```bash
pip3 install uv && uv sync
python main_create_lambda.py
```

### Step 4: Run the Example

```bash
python main.py
```

You should see output indicating that the Lambda was invoked and the user was successfully found in the PostgreSQL database.

## Project Components

### `main.tf`
Defines the infrastructure:
- **AW SSecrets Manager**: Stores the Postgres connection URI.
- **PostgreSQL Provider**: Creates the `users` table in the database container.

### `add_user_lambda/`
Contains the Lambda function logic:
- `models.py`: SQLAlchemy ORM models.
- `lambda_handler.py`: Handler that retrieves secrets and inserts a random user.

### `main_create_lambda.py`
Automates the process of zipping the lambda folder and deploying it to LocalStack using `boto3`.

## Environment Variables

The `.env` file contains:

```
ENDPOINT_URL=http://localhost:4566
AWS_DEFAULT_REGION=us-east-1
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
DATABASE_URL=postgresql://myuser:mypassword@host.docker.internal:5432/mydb
```

## Clean Up

To remove everything:

```bash
terraform destroy -auto-approve
docker compose down -v
```

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
