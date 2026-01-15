# Google Cloud Run + Firebase Emulator Example

Minimal viable example to work with Google Cloud Run locally using Firebase Emulator Suite and Python. This example demonstrates how to create a containerized service that registers patients in Firestore.

## Project Structure

```
gcp-cloud-run/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── firebase.json
├── .firebaserc
├── firestore.rules
├── .env
├── main.py
├── pyproject.toml
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (optional, for dev container setup)
- Cloud Code extension for VS Code (optional, but recommended)

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder
2. Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Type and select: **Dev Containers: Reopen in Container**
4. Wait for the container to build and dependencies to install

The dev container includes:
- **Python 3.12**
- **Node.js 18** and **Java 17** (for Firebase Emulator)
- **Firebase Tools**
- **Google Cloud Code Extension** pre-installed

### Step 2: Start Firebase Emulators

Inside the dev container terminal, start Firestore:

```bash
firebase emulators:start
```

You should see:

```
┌───────────┬────────────────┬─────────────────────────────────┐
│ Emulator  │ Host:Port      │ View in Emulator UI             │
├───────────┼────────────────┼─────────────────────────────────┤
│ Firestore │ localhost:8081 │ http://localhost:4000/firestore │
└───────────┴────────────────┴─────────────────────────────────┘
```

### Step 3: Run the Cloud Run Service Locally

Open a **new terminal** and run main service directly (Inner Loop):

```bash
cd app && pip install -r requirements.txt
export PORT=8080
export FIRESTORE_EMULATOR_HOST=localhost:8081
python main.py
```

### Step 4: Test the Service

Open a **third terminal** and run the client script:

```bash
python main.py
```

You should see:

```
Connecting to Cloud Run Service at http://localhost:8080...
Admitting patient: Jane Doe...
Success! Patient admitted.
```

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Prerequisites

1. **Install Node.js 18+ and Java 17+**
2. **Install Firebase CLI**: `npm install -g firebase-tools`
3. **Install Python Dependencies**:

```bash
pip3 install uv && uv sync
```

### Step 2: Start Emulators

```bash
firebase emulators:start
```

### Step 3: Run Service

In a new terminal:

```bash
cd app
pip3 install -r requirements.txt
export FIRESTORE_EMULATOR_HOST=localhost:8081
python3 main.py
```

### Step 4: Run the Client

In another terminal:

```bash
python3 main.py
```

## Project Components

### Cloud Run Service (`app/main.py`)

A Flask application acting as a microservice:

- **`admit_patient`**: Endpoint receiving POST requests with patient data.
- **Firestore Integration**: Connects to Firestore to save the data.
- **Automatic Environment Detection**: Uses `FIRESTORE_EMULATOR_HOST` to connect to the emulator automatically.

### Dockerfile (`app/Dockerfile`)

Defines the container image for Cloud Run:

- Uses `python:3.12-slim` base image.
- Installs dependencies from `requirements.txt`.
- Uses `gunicorn` as the production WSGI server.
- Exposes port 8080.

### Firestore Rules (`firestore.rules`)

Simple security rules for local development:
- Allows read/write access to all documents.

## Environment Variables

The `.env` file contains:

```
GCP_PROJECT_ID=demo-project
SERVICE_URL=http://localhost:8080
FIRESTORE_EMULATOR_HOST=localhost:8081
PORT=8080
```

**Note**: `FIRESTORE_EMULATOR_HOST` is crucial for the Python client to find the local emulator.

## Useful Commands

### Docker Commands

```bash
# Build the container
docker build -t patient-service ./app

# Run the container (connecting to host emulator requires network config)
docker run -p 8080:8080 --net=host -e FIRESTORE_EMULATOR_HOST=localhost:8081 patient-service
```

### Firebase Commands

```bash
# Start only Firestore
firebase emulators:start --only firestore
```

## Troubleshooting

### Emulator Port Conflict

If port 8081 is in use, change it in `firebase.json` and update `.env`.

### Service Cannot Connect to Firestore

Ensure `FIRESTORE_EMULATOR_HOST` is set in the terminal running the service.

## Clean Up

```bash
# Stop emulators (Ctrl+C)
docker system prune
```

## Next Steps

- Deploy to Google Cloud Run
- Add authentication
- Add data validation

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
