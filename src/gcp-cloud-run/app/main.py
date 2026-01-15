import os
from flask import Flask, request, jsonify
from google.cloud import firestore
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize Firestore client
# In local dev with emulator, this connects automatically if FIRESTORE_EMULATOR_HOST is set
db = firestore.Client(project=os.getenv("GCP_PROJECT_ID", "demo-project"))

@app.route("/", methods=["POST"])
def admit_patient():
    """Admit a new patient to the hospital."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        required_fields = ["name", "surname", "dni", "age", "gender"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Add timestamp
        data["admitted_at"] = firestore.SERVER_TIMESTAMP

        # Save to Firestore 'patients' collection
        doc_ref = db.collection("patients").document(data["dni"])
        doc_ref.set(data)

        return jsonify({
            "status": "success",
            "message": f"Patient {data['name']} {data['surname']} admitted successfully.",
            "patient_id": data["dni"]
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Use PORT env variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
