# Ejemplos Mínimos Viables (MVE)

Este repositorio enseña cómo desarrollar para el Cloud gratis, sin cuenta y sin tarjeta de crédito, emulando AWS, Azure y Google Cloud en local:

* ✅ **Gratis y sin cuenta**: Todas las tecnologías son gratis y no requieren de crear una cuenta en ningún sitio.
* **💯% compatible**: El código que desarrollas en local es 100% compatible con el Cloud real.
* 📦 **Autocontenido**: Cada ejemplo es independiente e incluye todo lo necesario para ejecutarlo.
* 🚀 **Listo para ejecutar**: Los ejemplos están listos para ejecutar sin hacer cambios en el código.
* 🐳 **Dockerizado**: Todos cuentan con entornos de desarrollo dockerizados.
* 🖥️ **Interfaces gráficas**: Uso de herramientas gráficas para gestionar el entorno Cloud local.
* 📖 **Bien documentado**: Todos los ejemplos están documentados en inglés y español.

## 🚀 Inicio Rápido

1. **Requisitos previos:**
    1. [Docker](https://www.docker.com/get-started) instalado y ejecutándose.
    2. [Extensión Dev Containers](vscode:extension/ms-vscode-remote.remote-containers) instalada.

2. **Abrir un ejemplo:** Abre una carpeta de ejemplo (ej. `src/aws-dynamo-db`) en VS Code.
3. **Reabrir en Contenedor:** Abre la **Paleta de Comandos** (`F1` o `Ctrl/Cmd+Shift+P`) y selecciona **Dev Containers: Reopen in Container**.
4. **Sigue las instrucciones:** Una vez que el contenedor esté listo, sigue las instrucciones en el `README.md` del ejemplo. Normalmente es solo:
   ```bash
   python main.py
   ```

## 📚 Ejemplos Disponibles

Algunos ejemplos aparecen varias veces en la tabla porque integran varios servicios cloud.

| Cloud | Servicio | MVE | Descripción | Tecnologías |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | Dynamo DB | [aws-dynamo-db](./src/aws-dynamo-db/) | Desarrollo local de AWS DynamoDB con LocalStack (Terraform/CloudFormation) | DynamoDB, S3, Lambda, Terraform, CloudFormation, LocalStack, Python |
| **AWS** | Dynamo DB | [aws-step-functions](./src/aws-step-functions/) | Desarrollo local de AWS Step Functions con LocalStack | Step Functions, Lambda, DynamoDB, LocalStack, Python |
| **AWS** | Lambda | [aws-dynamo-db](./src/aws-dynamo-db/) | Desarrollo local de AWS DynamoDB con LocalStack (Terraform/CloudFormation) | DynamoDB, S3, Lambda, Terraform, CloudFormation, LocalStack, Python |
| **AWS** | Lambda | [aws-step-functions](./src/aws-step-functions/) | Desarrollo local de AWS Step Functions con LocalStack | Step Functions, Lambda, DynamoDB, LocalStack, Python |
| **AWS** | Lambda | [localstack-docker](./src/localstack-docker/) | Configuración de LocalStack con servicios Lambda y S3 | LocalStack, Lambda, S3, Docker, Python |
| **AWS** | RDS (Postgres) | [localstack-hybrid-cloud](./src/localstack-hybrid-cloud/) | Escenario de nube híbrida con LocalStack y Postgres externo | LocalStack, Terraform, Secrets Manager, PostgreSQL, Docker, Python |
| **AWS** | S3 | [aws-dynamo-db](./src/aws-dynamo-db/) | Desarrollo local de AWS DynamoDB con LocalStack (Terraform/CloudFormation) | DynamoDB, S3, Lambda, Terraform, CloudFormation, LocalStack, Python |
| **AWS** | S3 | [localstack-docker](./src/localstack-docker/) | Configuración de LocalStack con servicios Lambda y S3 | LocalStack, Lambda, S3, Docker, Python |
| **AWS** | Step Functions | [aws-step-functions](./src/aws-step-functions/) | Desarrollo local de AWS Step Functions con LocalStack | Step Functions, Lambda, DynamoDB, LocalStack, Python |
| **Azure** | Azure Functions | [azure-functions](./src/azure-functions/) | Desarrollo local de Azure Functions con Azurite | Azure Functions, Azurite, Blob Storage, Docker, Python |
| **Azure** | Blob Storage | [azure-functions](./src/azure-functions/) | Desarrollo local de Azure Functions con Azurite | Azure Functions, Azurite, Blob Storage, Docker, Python |
| **Azure** | Blob Storage | [azurite-docker](./src/azurite-docker/) | Configuración de Azurite con emulación de Azure Blob Storage | Azurite, Azure, Blob Storage, Docker, Python |
| **Azure** | Cosmos DB | [azure-cosmos-db](./src/azure-cosmos-db/) | Desarrollo local de Azure Cosmos DB con Docker | Cosmos DB, Docker, Python |
| **Azure** | Databricks | [databricks-docker](./src/databricks-docker/) | Emulación local de Databricks con Docker, Spark y Delta Lake | Databricks, Spark, Delta Lake, Docker, Python |
| **GCP** | Cloud Functions | [gcp-functions](./src/gcp-functions/) | Desarrollo local de Google Cloud Functions con Firebase Emulator Suite | Google Cloud Functions, Firebase, Cloud Storage, Python |
| **GCP** | Cloud Run | [gcp-cloud-run](./src/gcp-cloud-run/) | Desarrollo local de Google Cloud Run con Firebase Emulator Suite | Cloud Run, Firebase, Firestore, Docker, Python |
| **GCP** | Cloud Storage | [gcp-functions](./src/gcp-functions/) | Desarrollo local de Google Cloud Functions con Firebase Emulator Suite | Google Cloud Functions, Firebase, Cloud Storage, Python |
| **GCP** | Firestore | [gcp-cloud-run](./src/gcp-cloud-run/) | Desarrollo local de Google Cloud Run con Firebase Emulator Suite | Cloud Run, Firebase, Firestore, Docker, Python |
| **Hybrid** | Airflow | [airflow-docker](./src/airflow-docker/) | Configuración de Apache Airflow con Docker Compose y Python | Apache Airflow, Docker, Python |
| **Hybrid** | Metabase | [metabase-docker](./src/metabase-docker/) | Configuración de Metabase con Docker Compose y PostgreSQL | Metabase, PostgreSQL, Docker, Python |
| **Hybrid** | MinIO | [minio-docker-boto3](./src/minio-docker-boto3/) | Configuración de MinIO con Docker Compose y Boto3 | MinIO, Docker, Boto3, Python |
| **Hybrid** | MinIO | [minio-docker-delta](./src/minio-docker-delta/) | Configuración de MinIO con Docker Compose y Delta Lake | MinIO, Delta Lake, Docker, Python |
| **Hybrid** | Mongo | [mongo-docker-mongoengine](./src/mongo-docker-mongoengine/) | Configuración de MongoDB con Docker Compose y ODM mongoengine | MongoDB, Docker, mongoengine, Python |
| **Hybrid** | Postgres | [localstack-hybrid-cloud](./src/localstack-hybrid-cloud/) | Escenario de nube híbrida con LocalStack y Postgres externo | LocalStack, Terraform, Secrets Manager, PostgreSQL, Docker, Python |
| **Hybrid** | Postgres | [postgres-docker-sqlalchemy](./src/postgres-docker-sqlalchemy/) | Configuración de PostgreSQL con Docker Compose y ORM SQLAlchemy | PostgreSQL, Docker, SQLAlchemy, Python |
| **Hybrid** | RabbitMQ | [rabbitmq-docker-pika](./src/rabbitmq-docker-pika/) | Configuración de RabbitMQ con Docker Compose y Python | RabbitMQ, Docker, Python |
| **Hybrid** | Redis | [redis-docker](./src/redis-docker/) | Configuración de Redis con Docker Compose y Python | Redis, Docker, Python |
| **Hybrid** | Redis | [redis-docker-mutex](./src/redis-docker-mutex/) | Mutex distribuido usando Redis con Docker Compose | Redis, Docker, Python |
| - | Dev Containers | [devcontainers-docker](./src/devcontainers-docker/) | Entendiendo DevContainers con Python y pandas | DevContainers, Docker, Python, VS Code |

_Más ejemplos próximamente..._

## 📝 Licencia

Este es un ejemplo mínimo para fines educativos. Siéntete libre de usarlo y modificarlo según sea necesario.

## 🌐 Sígueme

Conéctate conmigo en LinkedIn para más contenido y actualizaciones:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raulcastillabravo/)

---

**¡Feliz programación! 🚀**

Si encuentras estos ejemplos útiles, por favor considera darle una ⭐ a este repositorio
