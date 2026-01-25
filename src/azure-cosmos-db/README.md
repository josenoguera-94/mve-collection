# Azure Cosmos DB + Docker

Minimal viable example to work with Azure Cosmos DB locally using Docker. This example demonstrates how to integrate a Python application with the Azure Cosmos DB Emulator.

## Project Structure

```
azure-cosmos-db/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── docker-compose.yml
├── .env
├── main.py
├── pyproject.toml
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (optional, for dev container setup)

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder
2. Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Type and select: **Dev Containers: Reopen in Container**
4. Wait for the container to build and dependencies to install

### Step 2: Run the Example

```bash
python main.py
```

You should see output like:

```
--- Cosmos DB Connection Test ---
Endpoint: http://localhost:8081
Connecting to database: TestDB...
Connecting to container: TestContainer...
Uploading test item with ID: ...
SUCCESS: Item uploaded successfully to Cosmos DB!
```

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Python Dependencies

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv sync
```

### Step 2: Start the Emulator

```bash
docker compose up -d cosmos
```

### Step 3: Run the Example

```bash
python main.py
```

## Project Components

### Main Script (`main.py`)

Python script that demonstrates how to connect and interact with Cosmos DB:

- **CosmosClient**: Connects to the emulator using environment variables.
- **`run()`**: Main function that creates a database, a container, and upserts a test item.

## Environment Variables

The `.env` file contains:

```
COSMOS_ENDPOINT=http://localhost:8081
COSMOS_KEY=C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==
```

**Note**: The key is the default master key for the Cosmos DB emulator.

## Useful Commands

### Docker Commands

```bash
# Start emulator
docker compose up -d cosmos

# Stop emulator
docker compose down

# View logs
docker compose logs -f cosmos
```

## Troubleshooting

### Connection Refused

Make sure the emulator is running:
```bash
docker ps
```

### Evaluation period has expired / PAL initialization failed

If you see `Error: The evaluation period has expired` or `PAL initialization failed. Error: 104`, it means the emulator image's 180-day evaluation period has ended. 

**Official Fix (Pull latest image):**
1.  Stop everything: `docker compose down -v`
2.  Remove the old image: `docker rmi mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator`
3.  Pull the latest: `docker pull mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest`
4.  Start again: `docker compose up -d cosmos`

**Workaround (Use a specific tag):**
If Microsoft hasn't updated the `latest` image and the official fix doesn't work, find a specific and recent version tag from the official repository:
1. Go to [Azure Cosmos DB Emulator Docker Releases](https://github.com/Azure/azure-cosmos-db-emulator-docker/releases).
2. Look for the most recent tag (e.g., `vnext-EN20251223`).
3. Update the image in `docker-compose.yml` with that tag.
4. Start again: `docker compose up -d cosmos`

## Clean Up

To completely remove everything:

```bash
docker compose down -v
```

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
