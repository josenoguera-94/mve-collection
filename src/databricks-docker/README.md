# Databricks Local with Docker (Spark + Delta + Unity Catalog Sim)

High-fidelity local Databricks environment using Docker. It emulates Databricks 14.3/15.x LTS Runtime (Apache Spark 3.5.2 + Delta Lake 3.2.0) with local Cloud Storage (MinIO) and persistent Metastore (PostgreSQL for Unity Catalog simulation).

## Project Structure

```
databricks-docker/
├── src/
│   ├── databricks_shim/   # Abstraction layer (Local vs Cloud)
│   └── jobs/              # ETL Logic
├── Dockerfile             # Custom DBR-like image
├── docker-compose.yml     # Orchestration (Spark, MinIO, Postgres)
├── .env                   # Environment config
├── requirements.txt       # Python dependencies
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed

## Option 1: Using Docker Compose

### Step 1: Build and Start

This will build the custom Spark image and start MinIO and Postgres.

```bash
docker compose up -d --build
```

### Step 2: Create Storage Bucket

1. Open the MinIO Console: http://localhost:9001
2. Login with: User: `minioadmin` / Pass: `minioadmin`
3. Go to **Buckets** -> **Create Bucket**.
4. Create a bucket named: `demo-bucket` (**CRITICAL**: The ETL job will fail if this bucket doesn't exist).

### Step 3: Run the ETL Job

Execute the sample ETL which:
1. Generates data and writes to Bronze (MinIO)
2. Transforms and writes to Silver (Delta Table in Metastore)
3. Registers the table in the persistent Hive Metastore

```bash
docker compose exec spark python3 src/jobs/etl_sample.py
```

You should see:
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

### Step 3: Verify Persistence

1. **MinIO Console**: http://localhost:9001 (User/Pass: `minioadmin`)
   - Check `demo-bucket` for `bronze/` and `silver/` folders.
2. **Spark output**: The `SELECT` query confirms the Metastore is working.

## Project Components

### Custom Image (`Dockerfile`)

We build a custom image FROM `databricksruntime/python:latest` and manually install:
- **OpenJDK 17**: Required for Spark 3.5+
- **Apache Spark 3.5.2**: Matches DBR 15.x LTS
- **Delta Lake 3.2.0**: For ACID transactions
- **Hadoop AWS**: For S3A file system support

### Shim Layer (`src/databricks_shim/`)

Allows writing portable code:
- **`connect.py`**: Detects `APP_ENV`. If `local`, injects MinIO, Delta, and Postgres configurations into `SparkSession`.
- **`utils.py`**: Mocks `dbutils` (Secrets, Widgets) using environment variables when running locally.

### Infrastructure

- **MinIO**: Emulates S3 / ADLS Gen2.
- **PostgreSQL**: Acts as the persistent Hive Metastore (simulating Unity Catalog tables).

## Environment Variables

The `.env` file configures credentials and endpoints:

```
AWS_ENDPOINT_URL=http://minio:9000
POSTGRES_HOST=postgres
APP_ENV=local
```

## Clean Up

```bash
docker compose down -v
```

## License

Minimal viable example for educational purposes.
