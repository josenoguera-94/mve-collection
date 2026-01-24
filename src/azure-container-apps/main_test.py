import os
import uuid
from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configuration from .env or defaults
URL = 'http://localhost:8081' #os.getenv("COSMOS_ENDPOINT", "http://localhost:8081")
KEY = os.getenv("COSMOS_KEY", "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==")
DATABASE_NAME = "TestDB"
CONTAINER_NAME = "TestContainer"

def run_test():
    print(f"--- Cosmos DB Connection Test ---")
    print(f"Endpoint: {URL}")
    
    try:
        # Initialize Client
        # We use connection_verify=False to avoid SSL issues with the self-signed certificate on the host
        client = CosmosClient(URL, credential=KEY, connection_verify=False)
        
        print(f"Connecting to database: {DATABASE_NAME}...")
        database = client.create_database_if_not_exists(id=DATABASE_NAME)
        
        print(f"Connecting to container: {CONTAINER_NAME}...")
        container = database.create_container_if_not_exists(
            id=CONTAINER_NAME, 
            partition_key=PartitionKey(path="/category"),
            offer_throughput=400
        )
        
        # Prepare a test item
        test_id = str(uuid.uuid4())
        test_item = {
            "id": test_id,
            "category": "testing",
            "message": "Hello from local Python script!",
            "status": "verified"
        }
        
        print(f"Uploading test item with ID: {test_id}...")
        container.upsert_item(test_item)
        
        print(f"\033[92mSUCCESS: Item uploaded successfully to Cosmos DB!\033[0m")
        
    except Exception as e:
        print(f"\033[91mFAILURE: Could not connect or upload to Cosmos DB.\033[0m")
        print(f"Error detail: {e}")

if __name__ == "__main__":
    run_test()
