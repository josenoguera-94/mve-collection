# Ejemplo Google Cloud Run + Firebase Emulator

Ejemplo mínimo viable para trabajar con Google Cloud Run localmente usando Firebase Emulator Suite y Python. Este ejemplo demuestra cómo crear un servicio contenerizado que registra pacientes en Firestore.

## Estructura del Proyecto

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

## Prerrequisitos

- **Docker y Docker Compose** instalados
- **VS Code**

## Opción 1: Usando Dev Container (Rápido y Simple)

> **⚠️ LIMITACIONES:** Esta opción usa **Docker** directamente para ejecutar el servicio. **NO** usa Cloud Code ni Minikube.
> - **Pros**: Configuración rápida, sin complejidad, funciona de inmediato.
> - **Contras**: Sin "Hot Reload" (requiere reconstruir al cambiar código), sin simulación real de infraestructura (YAML, comportamiento Knative), sin depuración integrada.
> - **Recomendado para**: Pruebas rápidas de lógica de código e integración con Firestore.
> 
> **Para un entorno profesional completo con Minikube/Cloud Code, ver Opción 2.**

### Paso 1: Abrir el Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto.
2. Presiona `F1` -> **Dev Containers: Reopen in Container**.

El contenedor incluye Python, Node.js, Java y Firebase Tools.

### Paso 2: Iniciar Emuladores de Firebase

Dentro de la terminal del dev container:

```bash
firebase emulators:start
```

### Paso 3: Ejecutar el Servicio (Docker)

Abre una **nueva terminal** dentro de VS Code:

```bash
# Construir la imagen
docker build -t patient-service ./app

# Ejecutar el contenedor (network=host para acceder al Emulador Firebase)
docker run --rm -p 8080:8080 --net=host -e FIRESTORE_EMULATOR_HOST=localhost:8081 patient-service
```

### Paso 4: Probar el Servicio

Abre una **tercera terminal**:

```bash
# Opción A: usando script de python
python main.py

# Opción B: usando curl
curl -v -X POST http://localhost:8080 \
     -H "Content-Type: application/json" \
     -d '{"name": "Test", "surname": "User", "dni": "12345678X", "age": 30, "gender": "Female"}'
```

---

## Opción 2: Configuración Local (Profesional / Cloud Code)

Esta opción imita el entorno real de Cloud usando **Minikube** y **Cloud Code**. Ideal para desarrollo profundo.

### Paso 1: Instalar Prerrequisitos

Aunque Cloud Code puede intentar instalar dependencias, **se recomienda la instalación manual** para mayor estabilidad.

#### Linux (Debian/Ubuntu)
1. **Python (Mín v3.12)**:
   ```bash
   sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv
   ```
2. Asegúrate de tener `curl` instalado:
   ```bash
   sudo apt-get install -y curl
   ```
3. **Node.js v24**: [Guía de Instalación](https://nodesource.com/products/distributions)
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

4. **Java JDK v21**: [Descargar (Oracle)](https://www.oracle.com/es/java/technologies/downloads/)
   ```bash
   sudo apt-get update && sudo apt-get install -y openjdk-21-jdk
   ```

5. **Google Cloud CLI**: [Guía de Instalación](https://cloud.google.com/sdk/docs/install)
   ```bash
   sudo apt-get install -y apt-transport-https ca-certificates gnupg curl
   curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
   echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
   sudo apt-get update && sudo apt-get install -y google-cloud-cli google-cloud-cli-skaffold
   ```

6. **Minikube**: [Guía de Instalación](https://minikube.sigs.k8s.io/docs/start/)
   ```bash
   curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
   ```

7. **Firebase CLI**:
   ```bash
   sudo npm install -g firebase-tools
   ```

#### Windows
1. **Python (Mín v3.12)**: [Descargar](https://www.python.org/downloads/)
2. **Node.js (Mín v18)**: [Descargar](https://nodejs.org/en/download/)
3. **Java JDK (Mín v17)**: [Descargar (Oracle)](https://www.oracle.com/es/java/technologies/downloads/)
4. **Google Cloud CLI**: [Guía de Instalación](https://cloud.google.com/sdk/docs/install)
5. **Minikube**:
   ```powershell
   winget install Kubernetes.minikube
   ```
6. **Firebase CLI**:
   ```powershell
   npm install -g firebase-tools
   ```

#### macOS
1. **Python (Mín v3.12)**: [Descargar](https://www.python.org/downloads/)
2. **Node.js (Mín v18)**: [Descargar](https://nodejs.org/en/download/)
3. **Java JDK (Mín v17)**: [Descargar (Oracle)](https://www.oracle.com/es/java/technologies/downloads/)
4. **Google Cloud CLI**: [Guía de Instalación](https://cloud.google.com/sdk/docs/install)
5. **Minikube**:
   ```bash
   brew install minikube
   ```
6. **Firebase CLI**:
   ```bash
   sudo npm install -g firebase-tools
   ```

7. **Instalar Extensión VS Code**: Busca "Google Cloud Code" en VS Code e instálala.

### Paso 2: Configurar Proyecto

1. **Instalar Dependencias de Python**:
   Se recomienda usar el instalador independiente de `uv` para evitar conflictos con el sistema.

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

### Paso 3: Iniciar Emuladores

```bash
firebase emulators:start
```

### Paso 4: Ejecutar con Cloud Code

1. Haz clic en el icono de **Cloud Code** en la barra de actividad.
2. Expande **Cloud Run**.
3. Haz clic en **Run on Cloud Run Emulator** (icono de play).
   - > **Nota**: Si te pregunta para habilitar **minikube gcp-auth addon**, selecciona **Yes**. Si te pide **Iniciar Sesión** en Google Cloud, puedes **Cancelar** para mantenerlo 100% local.
   - > **Usuarios Linux**: Si falla la conexión, cambia `FIRESTORE_EMULATOR_HOST` en `.vscode/launch.json` a `host.minikube.internal:8081` o `172.17.0.1:8081`. El valor por defecto `host.docker.internal` está optimizado para Windows/WSL/macOS.
   - Cloud Code usará `skaffold` para construir y desplegar en tu Minikube local.
   - **Hot Reload** está activo: guarda un archivo y se actualiza automáticamente.

### Paso 5: Probar

```bash
# Opción A: usando script de python
python3 main.py

# Opción B: usando curl
curl -v -X POST http://localhost:8080 \
     -H "Content-Type: application/json" \
     -d '{"name": "Test", "surname": "User", "dni": "12345678X", "age": 30, "gender": "Female"}'
```

## Componentes del Proyecto

### Servicio Cloud Run (`app/main.py`)
App Flask que recibe datos de pacientes y escribe en Firestore. Autodetecta el emulador vía `FIRESTORE_EMULATOR_HOST`.

### Dockerfile (`app/Dockerfile`)
Contenedor de producción usando `gunicorn`.

### Reglas Firestore (`firestore.rules`)
Reglas permisivas para desarrollo local.

## Variables de Entorno

El archivo `.env` contiene:

```
GCP_PROJECT_ID=demo-project
SERVICE_URL=http://localhost:8080
FIRESTORE_EMULATOR_HOST=localhost:8081
PORT=8080
```

## Comandos Útiles

```bash
# Detener contenedores
docker system prune

# Detener Minikube
minikube stop
```

## Licencia

Este es un ejemplo mínimo para fines educativos. Siéntete libre de usarlo y modificarlo según sea necesario.
