# AWS Step Functions Local Development

Minimal viable example to work with **AWS Step Functions** locally using **LocalStack** and **VS Code AWS Toolkit**. This example demonstrates a user onboarding workflow with parallel Lambda execution and IAM user creation.

## Project Structure

```
aws-step-functions/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── lambdas/
│   ├── log_user.py          # Writes to DynamoDB
│   └── validate_email.py    # Validates email format
├── deploy.py                # Infrastructure deployment script
├── docker-compose.yml       # LocalStack services
├── main.py                  # Workflow execution script
├── pyproject.toml
├── step_function.asl.json   # Step Function definition (ASL)
├── utils.py                 # Utilities for ZIP and config
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (Recommended)
- [AWS Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-aws-us.aws-toolkit-vscode) (Included in Dev Container)

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder.
2. Press `F1` and select: **Dev Containers: Reopen in Container**.
3. Wait for the build to finish.

### Step 2: Start LocalStack

```bash
docker compose up -d
```

### Step 3: Deploy Infrastructure

```bash
python deploy.py
```

### Step 4: Wait for Lambda Initialization

Wait **5-10 seconds** for LocalStack to finish initializing the Lambda environment.

### Step 5: Run the Workflow

```bash
python main.py
```

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Dependencies

```bash
pip3 install uv && uv sync
```

### Step 2: Install AWS Toolkit

Manually install the **AWS Toolkit** from the VS Code Marketplace.

### Step 3: Run Example

Follow the same steps as the Dev Container (Start LocalStack, Deploy, Run).

---

## Working with AWS Toolkit (Step Functions Editor)

This MVE is designed to showcase the ASL editor provided by the AWS Toolkit.

### 1. View/Edit the Step Function

1. Open `step_function.asl.json`.
2. Click the **"Render Graph"** icon (top right corner of the editor) to see a visual representation of the workflow.
3. You can modify the states and the graph will update in real-time.

### 2. Execute and Debug

LocalStack supports Step Functions execution. While the AWS Toolkit usually connects to a real AWS account, you can use `main.py` to trigger executions locally and see the logs in the terminal.

To debug a specific state:
1. Modify the input in `main.py`.
2. Check the LocalStack logs: `docker compose logs -f localstack`.

## Project Components

### Lambdas (`lambdas/`)

- **LogUserLambda**: Saves user data and timestamp to a DynamoDB table named `UserLogs`.
- **ValidateEmailLambda**: Checks if the provided email follows a valid regex pattern.

### Step Function (`step_function.asl.json`)

- **ProcessUserOnboarding**: A `Parallel` state that runs both Lambdas simultaneously.
- **CreateIAMUser**: A `Task` using the AWS SDK integration to create a local IAM user if the previous steps succeed.

## Environment Variables

The `.env` file contains:

```
AWS_REGION=us-east-1
LOCALSTACK_ENDPOINT=http://localhost:4566
DYNAMODB_TABLE=UserLogs
STEP_FUNCTION_NAME=UserOnboardingWorkflow
```

## Troubleshooting

### Lambda Function is in 'Pending' State

If you run `main.py` immediately after `deploy.py`, you might see this error:
`The operation cannot be performed at this time. The function is currently in the following state: Pending`

**Solution**: Wait 5-10 seconds for LocalStack to finish initializing the Lambda environment and run `main.py` again.

## Clean Up

To completely remove everything:

```bash
docker compose down -v
```

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
