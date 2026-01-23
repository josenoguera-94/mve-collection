# Azure Container Apps + Cosmos DB

Ejemplo mínimo viable para trabajar con Azure Container Apps y Azure Cosmos DB de forma local. Este ejemplo demuestra cómo desarrollar un microservicio que almacena datos en un emulador de Cosmos DB.

## Estructura del Proyecto

```
azure-container-apps/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── app/
│   ├── main.py          # API Flask
│   ├── Dockerfile       # Definición del contenedor de la app
│   └── requirements.txt # Dependencias de Python
├── docker-compose.yml   # Orquestación de App y Emulador de Cosmos
├── .env                 # Variables de entorno locales
├── main.py              # Script cliente de prueba
├── pyproject.toml       # Metadatos del proyecto
└── README.md
```

## Requisitos Previos

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (Recomendado)

## Opción 1: Uso de Dev Container (Recomendado)

### Paso 1: Abrir el Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto
2. Presiona `F1` y selecciona: **Dev Containers: Reopen in Container**
3. Espera a que los contenedores se levanten y las dependencias se instalen

### Paso 2: Ejecutar el Ejemplo

Dentro de la terminal del Dev Container, ejecuta el script de prueba:

```bash
python main.py
```

Deberías ver:
```
Status Code: 201
Response: {"status": "success", "message": "Saved to CosmosDB"}
```

## Opción 2: Configuración Local

### Paso 1: Instalar Dependencias

```bash
pip install uv && uv sync
```

### Paso 2: Levantar Servicios

```bash
docker-compose up -d
```

### Paso 3: Ejecutar la Prueba

```bash
python main.py
```

## Variables de Entorno

El archivo `.env` contiene:

```
COSMOS_ENDPOINT=https://localhost:8081
COSMOS_KEY=C2y6yDjf5/R+ob0N8...
```

## Solución de Problemas

### Error de Certificado SSL
El emulador de Cosmos DB utiliza un certificado autofirmado. En este MVE, utilizamos `PYTHONHTTPSVERIFY=0` en el `docker-compose.yml` para desactivar la verificación en desarrollo local.

### Tiempo de Arranque del Emulador
El emulador de Cosmos DB puede tardar entre 1 y 2 minutos en estar completamente listo. El servicio `app` está configurado para esperar al healthcheck del emulador.

## Limpieza

```bash
docker-compose down -v
```

## Licencia
Este es un ejemplo mínimo con fines educativos.
