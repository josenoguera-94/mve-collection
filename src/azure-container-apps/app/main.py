import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dapr State Store endpoint
DAPR_URL = f"http://localhost:3500/v1.0/state/statestore"

@app.route('/user', methods=['POST'])
def save_user():
    user_data = request.json
    # Dapr expects a list of key-value pairs for state management
    state = [{"key": user_data['username'], "value": user_data}]
    
    response = requests.post(DAPR_URL, json=state)
    
    if response.status_code == 204:
        return jsonify({"status": "success", "message": "User saved to CosmosDB"}), 201
    return jsonify({"status": "error", "message": "Failed to save to CosmosDB"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
