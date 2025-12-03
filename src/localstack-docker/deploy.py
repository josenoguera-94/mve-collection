import boto3
import os
import zipfile
from dotenv import load_dotenv

load_dotenv()

class LambdaDeployer:
    def __init__(self):
        self.endpoint_url = os.getenv("ENDPOINT_URL", "http://localhost:4566")
        self.region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
        self.internal_endpoint = os.getenv("LAMBDA_INTERNAL_ENDPOINT", "http://localstack:4566")
        self.lambda_client = boto3.client('lambda', endpoint_url=self.endpoint_url, region_name=self.region)
        self.role_arn = "arn:aws:iam::000000000000:role/lambda-role"

    def deploy(self, lambda_file_path, dependencies=None, function_name=None):
        """
        Deploy a Lambda function to LocalStack.
        
        Args:
            lambda_file_path: Path to the Lambda function file
            dependencies: List of dependency file paths to include in the zip
            function_name: Name for the Lambda function (defaults to filename without extension)
        """
        # Determine function name
        if function_name is None:
            function_name = os.path.splitext(os.path.basename(lambda_file_path))[0]
        
        # Create zip file
        zip_filename = f"{function_name}.zip"
        self._create_zip(zip_filename, lambda_file_path, dependencies or [])
        
        # Read zip content
        with open(zip_filename, 'rb') as f:
            zipped_code = f.read()
        
        # Prepare handler string
        module_name = os.path.splitext(os.path.basename(lambda_file_path))[0]
        handler_str = f"{module_name}.lambda_handler"
        
        # Delete existing function if it exists
        self._delete_lambda(function_name)
        
        # Create Lambda function
        self.lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.9',
            Role=self.role_arn,
            Handler=handler_str,
            Code={'ZipFile': zipped_code},
            Environment={'Variables': {'ENDPOINT_URL': self.internal_endpoint}}
        )
        
        print(f"Lambda function '{function_name}' deployed successfully!")
        
        # Cleanup
        self._remove_zip(zip_filename)

    def _create_zip(self, zip_filename, lambda_file_path, dependencies):
        """Create a zip file with the Lambda function and its dependencies."""
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
        
        print(f"Creating {zip_filename}...")
        with zipfile.ZipFile(zip_filename, 'w') as z:
            # Add the Lambda function
            z.write(lambda_file_path, arcname=os.path.basename(lambda_file_path))
            
            # Add dependencies
            for dep_path in dependencies:
                z.write(dep_path, arcname=os.path.basename(dep_path))

    def _delete_lambda(self, function_name):
        """Delete a Lambda function if it exists."""
        try:
            self.lambda_client.delete_function(FunctionName=function_name)
            print(f"Deleted existing Lambda function '{function_name}'.")
        except self.lambda_client.exceptions.ResourceNotFoundException:
            pass

    def _remove_zip(self, zip_filename):
        """Remove the zip file."""
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
