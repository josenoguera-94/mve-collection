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

- **Docker and Docker Compose** installed
- **VS Code**

## Option 1: Using Dev Container (Fast & Simple)

> **⚠️ LIMITATIONS:** This option uses **Docker** directly to run the service. It does **NOT** use Cloud Code or Minikube.
> - **Pros**: Fast setup, no complex configuration, works immediately.
> - **Cons**: No "Hot Reload" (requires rebuild on change), no real infrastructure simulation (YAML configuration, Knative behavior), no integrated debugging.
> - **Recommended for**: Quick testing of code logic and Firestore integration.
> 
> **For a full professional environment with Minikube/Cloud Code, see Option 2.**

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder.
2. Press `F1` -> **Dev Containers: Reopen in Container**.

The container includes Python, Node.js, Java, and Firebase Tools.

### Step 2: Start Firebase Emulators

Inside the dev container terminal:

```bash
firebase emulators:start
```

### Step 3: Run the Service (Docker)

Open a **new terminal** inside VS Code:

```bash
# Build the image
docker build -t patient-service ./app

# Run the container (network=host to access Firebase Emulator)
docker run --rm -p 8080:8080 --net=host -e FIRESTORE_EMULATOR_HOST=localhost:8081 patient-service
```

### Step 4: Test the Service

Open a **third terminal**:

```bash
# Option A: using python script
python main.py

# Option B: using curl
curl -v -X POST http://localhost:8080 \
     -H "Content-Type: application/json" \
     -d '{"name": "Test", "surname": "User", "dni": "12345678X", "age": 30, "gender": "Female"}'
```

---

## Option 2: Local Setup (Professional / Cloud Code)

This option mimics the real Cloud environment using **Minikube** and **Cloud Code**. Ideal for deep development.

### Step 1: Install Prerequisites

Even though Cloud Code can attempt to install dependencies, **manual installation is recommended** for stability.

#### Linux (Debian/Ubuntu)
Ensure `curl` is installed:
```bash
sudo apt-get install -y curl
```

1. **Python (Min v3.12)**:
   ```bash
   sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv
   ```

2. **Node.js v24**: [Install Guide](https://nodesource.com/products/distributions)
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

3. **Java JDK v21**: [Download (Oracle)](https://www.oracle.com/java/technologies/downloads/)
   ```bash
   sudo apt-get update && sudo apt-get install -y openjdk-21-jdk
   ```

4. **Google Cloud CLI**: [Install Guide](https://cloud.google.com/sdk/docs/install)
   ```bash
   sudo apt-get install -y apt-transport-https ca-certificates gnupg curl
   curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
   echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
   sudo apt-get update && sudo apt-get install -y google-cloud-cli google-cloud-cli-skaffold
   ```

5. **Minikube**: [Install Guide](https://minikube.sigs.k8s.io/docs/start/)
   ```bash
   curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
   ```

6. **Firebase CLI**:
   ```bash
   sudo npm install -g firebase-tools
   ```

#### Windows
1. **Python (Min v3.12)**: [Download](https://www.python.org/downloads/)
2. **Node.js (Min v18)**: [Download](https://nodejs.org/en/download/)
3. **Java JDK (Min v17)**: [Download (Oracle)](https://www.oracle.com/java/technologies/downloads/)
4. **Google Cloud CLI**: [Install Guide](https://cloud.google.com/sdk/docs/install)
5. **Minikube**:
   ```powershell
   winget install Kubernetes.minikube
   ```
6. **Firebase CLI**:
   ```powershell
   npm install -g firebase-tools
   ```

#### macOS
1. **Python (Min v3.12)**: [Download](https://www.python.org/downloads/)
2. **Node.js (Min v18)**: [Download](https://nodejs.org/en/download/)
3. **Java JDK (Min v17)**: [Download (Oracle)](https://www.oracle.com/java/technologies/downloads/)
4. **Google Cloud CLI**: [Install Guide](https://cloud.google.com/sdk/docs/install)
5. **Minikube**:
   ```bash
   brew install minikube
   ```
6. **Firebase CLI**:
   ```bash
   sudo npm install -g firebase-tools
   ```

7. **Install VS Code Extension**: Search for "Google Cloud Code" in VS Code and install it.

### Step 2: Setup Project

1. **Install Python Dependencies**:
   It is recommended to use the standalone installer for `uv` to avoid system conflicts.

   **Linux/macOS**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.local/bin/env
   uv sync
   ```

   **Windows**:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   uv sync
   ```

### Step 3: Start Emulators

```bash
firebase emulators:start
```

### Step 4: Run with Cloud Code

1. Click on the **Cloud Code** icon in VS Code activity bar.
2. Expand **Cloud Run**.
3. Click the **Run on Cloud Run Emulator** (play icon).
   - > **Note**: If asked to enable **minikube gcp-auth addon**, select **Yes**. If prompted to **Sign in** to Google Cloud, you can **Cancel** to keep it 100% local.
   - > **Linux Users**: If connection fails, change `FIRESTORE_EMULATOR_HOST` in `.vscode/launch.json` to `host.minikube.internal:8081` or `172.17.0.1:8081`. The default `host.docker.internal` is optimized for Windows/WSL/macOS.
   - Cloud Code will use `skaffold` to build and deploy to your local Minikube.
   - **Hot Reload** is active: save a file, and it updates automatically.

### Step 5: Test

```bash
# Option A: using python script
python3 main.py

# Option B: using curl
curl -v -X POST http://localhost:8080 \
     -H "Content-Type: application/json" \
     -d '{"name": "Test", "surname": "User", "dni": "12345678X", "age": 30, "gender": "Female"}'
```

## Project Components

### Cloud Run Service (`app/main.py`)
Flask app that receives patient data and writes to Firestore. Auto-detects emulator via `FIRESTORE_EMULATOR_HOST`.

### Dockerfile (`app/Dockerfile`)
Production-grade container using `gunicorn`.

### Firestore Rules (`firestore.rules`)
Permissive rules for local development.

## Environment Variables

The `.env` file contains:

```
GCP_PROJECT_ID=demo-project
SERVICE_URL=http://localhost:8080
FIRESTORE_EMULATOR_HOST=localhost:8081
PORT=8080
```

## Useful Commands

```bash
# Stop containers
docker system prune

# Stop Minikube
minikube stop
```

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.
