# Ejemplo de Azure Container Apps + Cosmos DB

Ejemplo mínimo viable para trabajar con Azure Container Apps y Azure Cosmos DB localmente. Este ejemplo demuestra cómo orquestar la infraestructura con Docker Compose y construir un contenedor de aplicación que confía automáticamente en el emulador de Cosmos DB.

## Estructura del Proyecto

```
azure-container-apps/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── app/
│   ├── main.py          # API Flask
│   ├── Dockerfile       # Contenedor de la aplicación con confianza SSL
│   └── requirements.txt # Dependencias de Python
├── certificates/        # Autogenerado por el healthcheck del emulador
├── docker-compose.yml   # Infraestructura (Cosmos DB + Dev)
├── .env                 # Variables de entorno
├── main.py              # Script cliente de prueba
├── pyproject.toml       # Metadatos del proyecto
└── README.md
```

## Requisitos Previos

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (opcional, para configuración de dev container)

## Opción 1: Uso de Dev Container (Recomendado)

### Paso 1: Abrir el Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto
2. Presiona `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Escribe y selecciona: **Dev Containers: Reopen in Container**
4. Espera a que el contenedor se construya y las dependencias se instalen

### Paso 2: Iniciar Infraestructura y Construir App

1. Inicia el emulador de Cosmos DB:
   ```bash
   docker compose up -d cosmos-emulator
   ```
2. Espera a que el emulador esté saludable (revisa con `docker ps`).
3. Construye la imagen de la aplicación:
   ```bash
   docker build -t aca-api -f app/Dockerfile .
   ```
4. Ejecuta el contenedor de la aplicación (usando `--network host` para facilitar la conectividad en Linux):
   ```bash
   docker run -d --name aca_app --network host aca-api
   ```

### Paso 3: Ejecutar el Ejemplo

```bash
python main.py
```

Deberías ver una salida como:

```
Sending request to http://localhost:8080/user...
Status Code: 201
Response: {
  "status": "success",
  "message": "Saved to CosmosDB"
}
```

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Dependencias de Python

```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.local/bin/env
   uv sync
```

### Paso 2: Iniciar Infraestructura

1. Inicia Cosmos DB:
   ```bash
   docker compose up -d cosmos-emulator
   ```
2. Espera a que el emulador esté saludable (revisa con `docker ps`).

### Paso 3: Instalar Certificado del Emulador

Para permitir que tu host local confíe en el certificado autofirmado del emulador, sigue estos pasos:

1. Descarga el certificado:
   ```bash
   curl --insecure https://localhost:8081/_explorer/emulator.pem > ~/emulatorcert.crt
   ```
2. Cópialo a la carpeta de certificados de confianza:
   ```bash
   sudo cp ~/emulatorcert.crt /usr/local/share/ca-certificates/
   ```
3. Actualiza el almacén de confianza del sistema:
   ```bash
   sudo update-ca-certificates
   ```

### Paso 4: Construir y Ejecutar la App

1. Construye la app (asegúrate de estar en la raíz del proyecto):
   ```bash
   docker build -t aca-api -f app/Dockerfile .
   ```
2. Ejecuta la app:
   ```bash
   docker run -d --name aca_app --network host aca-api
   ```

### Paso 5: Ejecutar el Ejemplo

```bash
python main.py
```

## Componentes del Proyecto

### API Flask (`app/main.py`)

Microservicio que recibe datos de usuario y los guarda en Cosmos DB:

- **CosmosClient**: Conecta al emulador usando variables de entorno.
- **`save_user()`**: Endpoint `/user` (POST) que inserta/actualiza datos en el contenedor "users".

### Script Principal (`main.py`)

Cliente de prueba que demuestra la integración:

- Paso 1: Define una carga JSON con información de usuario.
- Paso 2: Envía una solicitud POST a la API Flask.
- Paso 3: Imprime el estado y contenido de la respuesta.

## Variables de Entorno

El archivo `.env` contiene:

```
COSMOS_ENDPOINT=https://localhost:8081
COSMOS_KEY=C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==
```

**Nota**: La clave es la clave maestra por defecto para el emulador de Cosmos DB.

## Comandos Útiles

### Comandos de Docker

```bash
# Iniciar infraestructura
docker compose up -d cosmos-emulator

# Detener todo
docker compose down -v
docker stop aca_app && docker rm aca_app

# Ver logs de la app
docker logs aca_app
```

## Solución de Problemas

### Construcción de la App demasiado pronto

Si el `docker build` falla en el paso `COPY`, asegúrate de que el archivo `certificates/emulator.crt` exista. Solo se crea después de que el `cosmos-emulator` haya completado su primer healthcheck.

### Conexión Rechazada

Asegúrate de que tanto el emulador como la app estén en ejecución:
```bash
docker ps
```

### El periodo de evaluación ha expirado / Error 104 de PAL

Si ves el error `Error: The evaluation period has expired` o `PAL initialization failed. Error: 104`, significa que el periodo de evaluación de 180 días de la imagen ha caducado.

**Solución Oficial (Descargar imagen más reciente):**
1.  Detén todo: `docker compose down -v`
2.  Elimina la imagen antigua: `docker rmi mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator`
3.  Descarga la última versión: `docker pull mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest`
4.  Levanta de nuevo: `docker compose up -d cosmos-emulator`

**Solución Alternativa (Usar un tag específico):**
Si Microsoft aún no ha actualizado la imagen `latest` y la solución oficial no funciona, la solución más fiable es buscar una etiqueta de versión específica y reciente en el repositorio oficial:
1. Ve a [Azure Cosmos DB Emulator Docker Releases](https://github.com/Azure/azure-cosmos-db-emulator-docker/releases).
2. Busca el tag más reciente (ej. `vnext-EN20251223`).
3. Actualiza la imagen en `docker-compose.patch.yml` con ese tag.
4. Levanta usando el archivo de parche:
   ```bash
   docker compose -f docker-compose.patch.yml up -d
   ```

## Limpieza

Para eliminar todo completamente:

```bash
docker stop aca_app && docker rm aca_app
docker compose down -v
docker rmi aca-api
```

## Licencia

Este es un ejemplo mínimo con fines educativos. Siéntete libre de usarlo y modificarlo según sea necesario.
