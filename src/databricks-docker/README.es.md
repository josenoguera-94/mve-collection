# Databricks Local con Docker (Spark + Delta + Unity Catalog Sim)

Entorno Databricks local de alta fidelidad usando Docker. Emula el Runtime de Databricks 14.3/15.x LTS (Apache Spark 3.5.2 + Delta Lake 3.2.0) con Cloud Storage local (MinIO) y Metastore persistente (PostgreSQL para simulación de Unity Catalog).

## Estructura del Proyecto

```
databricks-docker/
├── src/
│   ├── databricks_shim/   # Capa de abstracción (Local vs Cloud)
│   └── jobs/              # Lógica ETL
├── Dockerfile             # Imagen personalizada tipo DBR
├── docker-compose.yml     # Orquestación (Spark, MinIO, Postgres)
├── .env                   # Configuración de entorno
├── requirements.txt       # Dependencias Python
└── README.md
```

## Requisitos Previos

- Docker y Docker Compose instalados

## Opción 1: Usando Docker Compose

### Paso 1: Construir e Iniciar

Esto construirá la imagen personalizada de Spark e iniciará MinIO y Postgres.

```bash
docker compose up -d --build
```

### Paso 2: Crear el Bucket de Almacenamiento

1. Abre la consola de MinIO: http://localhost:9001
2. Inicia sesión: Usuario: `minioadmin` / Password: `minioadmin`
3. Ve a **Buckets** -> **Create Bucket**.
4. Crea un bucket llamado: `demo-bucket` (**CRÍTICO**: El ETL fallará si este bucket no existe).

### Paso 3: Ejecutar el Job ETL

Ejecuta el ETL de ejemplo que:
1. Genera datos y los escribe en Bronze (MinIO)
2. Transforma y escribe en Silver (Tabla Delta en Metastore)
3. Registra la tabla en el Hive Metastore persistente

```bash
docker compose exec spark python3 src/jobs/etl_sample.py
```

Deberías ver:
```text
🚀 Starting ETL Job...
💾 Writing Bronze Layer...
💾 Writing Silver Layer...
✅ ETL Job Completed Successfully!
📊 Verification Query:
+---+---------+-----+----------+...
| id|     name|price|      date|...
+---+---------+-----+----------+...
```

### Paso 3: Verificar Persistencia

1. **MinIO Console**: http://localhost:9001 (User/Pass: `minioadmin`)
   - Revisa `demo-bucket` para ver carpetas `bronze/` y `silver/`.
2. **Salida Spark**: La consulta `SELECT` confirma que el Metastore funciona.

## Componentes del Proyecto

### Imagen Personalizada (`Dockerfile`)

Construimos una imagen FROM `databricksruntime/python:latest` e instalamos manualmente:
- **OpenJDK 17**: Requerido por Spark 3.5+
- **Apache Spark 3.5.2**: Coincide con DBR 15.x LTS
- **Delta Lake 3.2.0**: Para transacciones ACID
- **Hadoop AWS**: Para soporte de sistema de archivos S3A

### Capa Shim (`src/databricks_shim/`)

Permite escribir código portable:
- **`connect.py`**: Detecta `APP_ENV`. Si es `local`, inyecta configuraciones de MinIO, Delta y Postgres en la `SparkSession`.
- **`utils.py`**: Mockea `dbutils` (Secrets, Widgets) usando variables de entorno al ejecutar localmente.

### Infraestructura

- **MinIO**: Emula S3 / ADLS Gen2.
- **PostgreSQL**: Actúa como Hive Metastore persistente (simulando tablas Unity Catalog).

## Variables de Entorno

El archivo `.env` configura credenciales y endpoints:

```
AWS_ENDPOINT_URL=http://minio:9000
POSTGRES_HOST=postgres
APP_ENV=local
```

## Limpieza

```bash
docker compose down -v
```

## Licencia

Ejemplo mínimo viable con fines educativos.
