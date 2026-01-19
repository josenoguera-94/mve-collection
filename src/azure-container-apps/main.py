import requests
import json

def test_save_user():
    url = "http://localhost:8080/user"
    user_data = {
        "firstName": "Raúl",
        "lastName": "Castilla",
        "username": "rcastilla",
        "role": "Content Creator"
    }
    
    print(f"Sending user data for {user_data['username']}...")
    response = requests.post(url, json=user_data)
    
    if response.status_code == 201:
        print("Success: User registered in CosmosDB!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_save_user()
