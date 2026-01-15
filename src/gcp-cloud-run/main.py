import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Configuration
SERVICE_URL = os.getenv("SERVICE_URL", "http://localhost:8080")

def main():
    print(f"Connecting to Cloud Run Service at {SERVICE_URL}...")

    patient_data = {
        "name": "Jane",
        "surname": "Doe",
        "age": 32,
        "gender": "Female",
        "dni": "12345678X",
        "height": 170,
        "weight": 65,
        "phone": "+123456789"
    }

    print(f"Admitting patient: {patient_data['name']} {patient_data['surname']}...")
    
    try:
        response = requests.post(
            SERVICE_URL,
            json=patient_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 201:
            print("Success! Patient admitted.")
            print("Response:", response.json())
        else:
            print(f"Failed. Status: {response.status_code}")
            print("Response:", response.text)
            
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to {SERVICE_URL}. Is the service running?")

    print("\nCheck the Firebase Emulator UI at http://localhost:4000/firestore")

if __name__ == "__main__":
    main()
