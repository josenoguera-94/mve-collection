import os
import requests
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "demo-project")
FUNCTION_URL = f"http://localhost:5001/{PROJECT_ID}/us-central1/upload_file"

def main():
    print("Testing Firebase Cloud Function...")
    print(f"Function URL: {FUNCTION_URL}\n")
    
    payload = {
        "filename": "test.txt",
        "content": "Hello from Firebase Functions!"
    }
    
    print(f"Uploading '{payload['filename']}'...")
    response = requests.post(FUNCTION_URL, json=payload)
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("\nCheck the Firebase Emulator UI at http://localhost:4000")

if __name__ == "__main__":
    main()
