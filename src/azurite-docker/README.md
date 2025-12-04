# Azurite + Azure Blob Storage Example

Minimal viable example to work with Azure Blob Storage locally using Azurite, Docker Compose, and Python. This example demonstrates how to create containers and upload/download blobs.

## Project Structure

```
azurite-docker/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── docker-compose.yml
├── .env
├── azurite_client.py
├── main.py
├── pyproject.toml
├── uv.lock
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

The dev container includes the **Azurite extension** pre-installed.

### Step 2: Start Azurite

**Option A: Using Docker Compose**

Inside the dev container terminal:

```bash
docker compose up -d
```

Verify it's running:

```bash
docker ps
```

**Option B: Using Azurite VS Code Extension**

1. Press `F1` or `Ctrl+Shift+P`
2. Type and select: **Azurite: Start**
3. The extension will start Azurite services locally

You can also use the Azurite icon in the VS Code status bar to start/stop services.

### Step 3: Run the Example

```bash
python main.py
```

You should see output like:

```
Connecting to Azurite...
Container 'test-container' created.

Uploading blob...
Uploaded 'hello.txt' to container 'test-container'.

Listing blobs in container:
  - hello.txt

Downloading blob...
Content: Hello from Azurite!
```

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Python Dependencies

```bash
pip3 install uv && uv sync
```

### Step 2: Install Azurite Extension (Optional)

1. Open VS Code
2. Go to Extensions (`Ctrl+Shift+X`)
3. Search for "Azurite"
4. Install the extension by Microsoft

### Step 3: Start Azurite

**Option A: Using Docker Compose**

```bash
docker compose up -d
```

**Option B: Using Azurite Extension**

1. Press `F1` or `Ctrl+Shift+P`
2. Select: **Azurite: Start**

### Step 4: Run the Example

```bash
python main.py
```

## Project Components

### AzuriteClient (`azurite_client.py`)

Client class for Azure Blob Storage operations:

- **Constructor**: Reads connection string from environment variables and creates BlobServiceClient
- **`create_container(container_name)`**: Creates a container if it doesn't exist
- **`upload_blob(container_name, blob_name, data)`**: Uploads data to a blob
- **`download_blob(container_name, blob_name)`**: Downloads and returns blob content
- **`list_blobs(container_name)`**: Lists all blobs in a container

### Main Script (`main.py`)

Demonstrates Azurite Blob Storage operations:

- Creates a container
- Uploads a blob
- Lists all blobs in the container
- Downloads and displays blob content

## Environment Variables

The `.env` file contains:

```
# Azurite default connection string
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;

# Container name
CONTAINER_NAME=test-container
```

**Note**: The connection string uses Azurite's default credentials for local development.

## Azurite Extension Features

The Azurite VS Code extension provides:

- **Easy Start/Stop**: Control Azurite services from VS Code
- **Status Bar Integration**: See service status at a glance
- **Multiple Services**: Blob, Queue, and Table storage emulation
- **No Docker Required**: Can run Azurite without Docker

### Extension Commands

- `Azurite: Start` - Start all Azurite services
- `Azurite: Start Blob Service` - Start only Blob service
- `Azurite: Stop` - Stop all services
- `Azurite: Clean` - Clean Azurite data

## Useful Commands

### Docker Commands

```bash
# Start Azurite container
docker compose up -d

# Stop container
docker compose down

# Stop and remove volumes (delete all data)
docker compose down -v

# View logs
docker compose logs -f

# View only Azurite logs
docker compose logs -f azurite
```

### Azure Storage Explorer

You can also use [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/) to browse Azurite storage:

1. Download and install Azure Storage Explorer
2. Connect to Local Storage Emulator
3. Use the default Azurite connection string

## Troubleshooting

### Port Already in Use

If port 10000 is already in use, modify the `docker-compose.yml` ports section:

```yaml
ports:
  - "10010:10000"
```

Then update the connection string in `.env`:

```
BlobEndpoint=http://127.0.0.1:10010/devstoreaccount1
```

### Connection Refused

Make sure Azurite is running:

```bash
docker ps
```

Or check the Azurite extension status in VS Code status bar.

### Module Not Found

If you get import errors, install dependencies:

```bash
pip3 install uv && uv sync
```

## Clean Up

To completely remove everything:

```bash
# Stop and remove containers and volumes
docker compose down -v

# Remove the Azurite image (optional)
docker rmi mcr.microsoft.com/azure-storage/azurite
```

## Next Steps

- Add Queue storage examples
- Add Table storage examples
- Implement Azure Functions with Azurite
- Add unit tests for storage operations

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
