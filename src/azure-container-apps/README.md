# Azure Container Apps + Dapr + Cosmos DB

Minimal viable example to work with Azure Container Apps locally using Dapr and Cosmos DB Emulator. This example demonstrates how to create a microservice that registers users in Cosmos DB without an Azure subscription.

## Project Structure

```
azure-container-apps/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── components/
│   └── statestore.yaml
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── .env
├── main.py
├── pyproject.toml
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (optional)

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder.
2. Press `F1` and select: **Dev Containers: Reopen in Container**.
3. Wait for the services to build (this will automatically start the emulator and the app).

### Step 2: Run the Example

Inside the container terminal, run:

```bash
python main.py
```

You should see output indicating the user was saved successfully.

---

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Dependencies

```bash
pip3 install uv && uv sync
```

### Step 2: Start Infrastructure

```bash
docker-compose up -d
```

### Step 3: Run the Example

```bash
python main.py
```

---

## Project Components

### Flask API (`app/main.py`)

Microservice that receives user data. The magic here is it **doesn't use the Cosmos DB SDK**. It communicates with the Dapr sidecar via HTTP, making it fully portable.

### Dapr Configuration (`components/statestore.yaml`)

Defines the state store component. This is where we tell Dapr to use the Cosmos DB emulator. In production, you would only change this YAML to point to the real instance.

### Test Script (`main.py`)

Simulates an external request by sending a JSON with LinkedIn profile data.

---

## Environment Variables

The `.env` file contains:

```
COSMOS_KEY=C2y6yDjf5/...
COSMOS_URL=https://localhost:8081
```

**Note**: The emulator key is a standard, public key provided by Microsoft for local testing.

---

## Useful Commands

### Docker Commands

```bash
# View app logs
docker logs aca_app

# View Dapr sidecar logs
docker logs azure-container-apps-app-dapr-1

# Stop everything
docker-compose down
```

---

## Troubleshooting

### SSL Certificate Error

The Cosmos DB emulator uses self-signed certificates. Dapr is already configured to ignore validation in this dev environment.

### Data Explorer not loading

Ensure port `1234` is free. You can access the explorer at `http://localhost:1234` once the `cosmos_local` container is running.

---

## Clean Up

To completely remove the setup:

```bash
docker-compose down -v
docker rmi azure-container-apps-app
```

---

## Next Steps

- Implement Pub/Sub with Dapr and Redis.
- Add Dapr-managed secrets.
- Configure autoscaling with KEDA.

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
