import boto3
import json
import os
from dotenv import load_dotenv
from utils import create_lambda_zip, get_boto_config

load_dotenv()
config = get_boto_config()

def deploy():
    # 1. DynamoDB
    db = boto3.resource("dynamodb", **config)
    try:
        db.create_table(
            TableName=os.getenv("DYNAMODB_TABLE"),
            KeySchema=[{"AttributeName": "username", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "username", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
        )
        print("DynamoDB table created.")
    except db.meta.client.exceptions.ResourceInUseException: pass

    # 2. Lambdas
    lambda_client = boto3.client("lambda", **config)
    lambdas = ["log_user", "validate_email"]
    arns = {}
    
    role_arn = "arn:aws:iam::000000000000:role/lambda-role" # Mock role for LocalStack

    for name in lambdas:
        func_name = f"{name.replace('_', '-').title().replace('-', '')}Lambda"
        zip_content = create_lambda_zip(f"lambdas/{name}.py")
        
        try:
            res = lambda_client.create_function(
                FunctionName=func_name,
                Runtime="python3.12",
                Role=role_arn,
                Handler=f"{name}.handler",
                Code={"ZipFile": zip_content}
            )
            arns[f"{func_name}Arn"] = res["FunctionArn"]
        except lambda_client.exceptions.ResourceConflictException:
            arns[f"{func_name}Arn"] = f"arn:aws:lambda:{config['region_name']}:000000000000:function:{func_name}"

    # 3. Step Function
    sfn = boto3.client("stepfunctions", **config)
    with open("step_function.asl.json") as f:
        asl = f.read()
        for key, arn in arns.items():
            asl = asl.replace(f"${{{key}}}", arn)

    try:
        sfn.create_state_machine(
            name=os.getenv("STEP_FUNCTION_NAME"),
            definition=asl,
            roleArn=role_arn
        )
        print("Step Function created.")
    except sfn.exceptions.StateMachineAlreadyExists: pass

if __name__ == "__main__":
    deploy()
