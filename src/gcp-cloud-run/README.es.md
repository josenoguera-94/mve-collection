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

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (opcional, para configuración con contenedores)
- Extensión Cloud Code para VS Code (opcional, pero recomendada)

## Opción 1: Usando Dev Container (Recomendado)

### Paso 1: Abrir el Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto
2. Presiona `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Escribe y selecciona: **Dev Containers: Reopen in Container**
4. Espera a que el contenedor se construya y se instalen las dependencias

El dev container incluye:
- **Python 3.12**
- **Node.js 18** y **Java 17** (para Firebase Emulator)
- **Firebase Tools**
- **Extensión Google Cloud Code** preinstalada

### Paso 2: Iniciar Emuladores de Firebase

Dentro de la terminal del dev container, inicia Firestore:

```bash
firebase emulators:start
```

Deberías ver:

```
┌───────────┬────────────────┬─────────────────────────────────┐
│ Emulator  │ Host:Port      │ View in Emulator UI             │
├───────────┼────────────────┼─────────────────────────────────┤
│ Firestore │ localhost:8081 │ http://localhost:4000/firestore │
└───────────┴────────────────┴─────────────────────────────────┘
```

### Paso 3: Ejecutar el Servicio Cloud Run Localmente

Abre una **nueva terminal** y ejecuta el servicio principal directamente (Inner Loop):

```bash
cd app && pip install -r requirements.txt
export PORT=8080
export FIRESTORE_EMULATOR_HOST=localhost:8081
python main.py
```

### Paso 4: Probar el Servicio

Abre una **tercera terminal** y ejecuta el script cliente:

```bash
python main.py
```

Deberías ver:

```
Connecting to Cloud Run Service at http://localhost:8080...
Admitting patient: Jane Doe...
Success! Patient admitted.
```

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Prerrequisitos

1. **Instalar Node.js 18+ y Java 17+**
2. **Instalar Firebase CLI**: `npm install -g firebase-tools`
3. **Instalar Dependencias de Python**:

```bash
pip3 install uv && uv sync
```

### Paso 2: Iniciar Emuladores

```bash
firebase emulators:start
```

### Paso 3: Ejecutar Servicio

En una nueva terminal:

```bash
cd app
pip3 install -r requirements.txt
export FIRESTORE_EMULATOR_HOST=localhost:8081
python3 main.py
```

### Paso 4: Ejecutar el Cliente

En otra terminal:

```bash
python3 main.py
```

## Componentes del Proyecto

### Servicio Cloud Run (`app/main.py`)

Una aplicación Flask que actúa como microservicio:

- **`admit_patient`**: Endpoint que recibe peticiones POST con datos del paciente.
- **Integración Firestore**: Conecta a Firestore para guardar los datos.
- **Detección Automática de Entorno**: Usa `FIRESTORE_EMULATOR_HOST` para conectar al emulador automáticamente.

### Dockerfile (`app/Dockerfile`)

Define la imagen del contenedor para Cloud Run:

- Usa imagen base `python:3.12-slim`.
- Instala dependencias desde `requirements.txt`.
- Usa `gunicorn` como servidor WSGI de producción.
- Expone el puerto 8080.

### Reglas de Firestore (`firestore.rules`)

Reglas de seguridad simples para desarrollo local:
- Permite acceso de lectura/escritura a todos los documentos.

## Variables de Entorno

El archivo `.env` contiene:

```
GCP_PROJECT_ID=demo-project
SERVICE_URL=http://localhost:8080
FIRESTORE_EMULATOR_HOST=localhost:8081
PORT=8080
```

**Nota**: `FIRESTORE_EMULATOR_HOST` es crucial para que el cliente Python encuentre el emulador local.

## Comandos Útiles

### Comandos Docker

```bash
# Construir el contenedor
docker build -t patient-service ./app

# Ejecutar el contenedor (conectar al emulador host requiere config de red)
docker run -p 8080:8080 --net=host -e FIRESTORE_EMULATOR_HOST=localhost:8081 patient-service
```

### Comandos Firebase

```bash
# Iniciar solo Firestore
firebase emulators:start --only firestore
```

## Solución de Problemas

### Conflicto de Puertos del Emulador

Si el puerto 8081 está en uso, cámbialo en `firebase.json` y actualiza `.env`.

### El Servicio no Conecta a Firestore

Asegúrate de que `FIRESTORE_EMULATOR_HOST` esté configurado en la terminal que ejecuta el servicio.

## Limpieza

```bash
# Detener emuladores (Ctrl+C)
docker system prune
```

## Siguientes Pasos

- Desplegar en Google Cloud Run
- Añadir autenticación
- Añadir validación de datos

## Licencia

Este es un ejemplo mínimo para fines educativos. Siéntete libre de usarlo y modificarlo según sea necesario.
