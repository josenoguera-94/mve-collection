import os
from flask import Flask, request, jsonify
from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Cosmos DB configuration
URL = os.getenv("COSMOS_ENDPOINT")
KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "Inventory"
CONTAINER_NAME = "users"

# Initialize Client
client = CosmosClient(URL, credential=KEY)
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
