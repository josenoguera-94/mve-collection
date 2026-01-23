# Azure Container Apps + Cosmos DB

Minimal viable example to work with Azure Container Apps and Azure Cosmos DB locally. This example demonstrates how to develop a microservice that stores data in a Cosmos DB emulator.

## Project Structure

```
azure-container-apps/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── app/
│   ├── main.py          # Flask API
│   ├── Dockerfile       # App container definition
│   └── requirements.txt # Python dependencies
├── docker-compose.yml   # Orchestrates App and Cosmos Emulator
├── .env                 # Local environment variables
├── main.py              # Test client script
├── pyproject.toml       # Project metadata
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (Recommended)

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder
2. Press `F1` and select: **Dev Containers: Reopen in Container**
3. Wait for the containers to start and dependencies to install

### Step 2: Run the Example

Inside the Dev Container terminal, run the test script:

```bash
python main.py
```

You should see:
```
Status Code: 201
Response: {"status": "success", "message": "Saved to CosmosDB"}
```

## Option 2: Local Setup

### Step 1: Install Dependencies

```bash
pip install uv && uv sync
```

### Step 2: Start Services

```bash
docker-compose up -d
```

### Step 3: Run the Test

```bash
python main.py
```

## Environment Variables

The `.env` file contains:

```
COSMOS_ENDPOINT=https://localhost:8081
COSMOS_KEY=C2y6yDjf5/R+ob0N8...
```

## Troubleshooting

### SSL Certificate Error
The Cosmos DB emulator uses a self-signed certificate. In this MVE, we use `PYTHONHTTPSVERIFY=0` in the `docker-compose.yml` to disable verification for local development.

### Emulator Startup Time
The Cosmos DB emulator can take 1-2 minutes to be fully ready. The `app` service is configured to wait for the emulator's healthcheck.

## Clean Up

```bash
docker-compose down -v
```

## License
This is a minimal example for educational purposes.
