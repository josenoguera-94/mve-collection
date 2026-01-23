import requests
import json

# Terminal colors for better visibility
GREEN = "\033[92m"
RESET = "\033[0m"

API_URL = "http://localhost:8080/user"

def test_save_user():
    print(f"Sending request to {API_URL}...")
    
    user_payload = {
        "username": "raulcastilla",
        "email": "raul@example.com",
        "role": "admin"
    }
    
    response = requests.post(API_URL, json=user_payload)
    
    print(f"Status Code: {GREEN}{response.status_code}{RESET}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    test_save_user()
