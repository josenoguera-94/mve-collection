import os
from flask import Flask, request, jsonify
from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Cosmos DB configuration
# Default URL 'cosmos_local' works# When using --network host, the emulator is at localhost:8081
URL = os.getenv("COSMOS_ENDPOINT", "http://localhost:8081")
KEY = os.getenv("COSMOS_KEY", "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==")
DATABASE_NAME = "Inventory"
CONTAINER_NAME = "users"

print(f"Connecting to Cosmos DB at: {URL}")

try:
    # Initialize Client
# We use connection_verify=False for local dev to bypass certificate strictness
# which combined with the installed cert in the Dockerfile should fix the SSL issue.
    client = CosmosClient(URL, credential=KEY, connection_verify=False)
except Exception as e:
    print(f"Failed to initialize CosmosClient: {e}")
    raise
database = client.create_database_if_not_exists(id=DATABASE_NAME)
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME, 
    partition_key=PartitionKey(path="/username")
)

@app.route('/user', methods=['POST'])
def save_user():
    user_data = request.json
    user_data['id'] = user_data['username'] # Required by Cosmos
    container.upsert_item(user_data)
    return jsonify({"status": "success", "message": "Saved to CosmosDB"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
