#!/bin/bash
set -e

# Install uv and dependencies
pip3 install uv
uv sync

# Configure LocalStack profile for AWS CLI
aws configure set aws_access_key_id test --profile localstack
aws configure set aws_secret_access_key test --profile localstack
aws configure set region us-east-1 --profile localstack
aws configure set output json --profile localstack
aws configure set endpoint_url http://localhost:4566 --profile localstack

# Package Lambda function
python package_lambda.py

# Deploy Infrastructure
terraform init
terraform apply -auto-approve
