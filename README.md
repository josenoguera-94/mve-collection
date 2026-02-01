# Minimal Viable Examples (MVE)

This repository teaches how to develop for the Cloud for free, without an account and without a credit card, emulating AWS, Azure, and Google Cloud locally:

* ✅ **Free and account-less**: All technologies are free and do not require creating an account anywhere.
* **💯% compatible**: The code you develop locally is 100% compatible with the real Cloud.
* 📦 **Self-contained**: Each example is independent and includes everything necessary to run it.
* 🚀 **Ready to run**: Examples are ready to run without making code changes.
* 🐳 **Dockerized**: All have dockerized development environments.
* 🖥️ **Graphical interfaces**: Use of graphical tools to manage the local Cloud environment.
* 📖 **Well documented**: All examples are documented in English and Spanish.

## 🚀 Quick Start

1. **Prerequisites:**
    1. [Docker](https://www.docker.com/get-started) installed and running.
    2. [Dev Containers extension](vscode:extension/ms-vscode-remote.remote-containers) installed.

2. **Open an example:** Open an example folder (e.g., `src/aws-dynamo-db`) in VS Code.
3. **Reopen in Container:** Open the **Command Palette** (`F1` or `Ctrl/Cmd+Shift+P`) and select **Dev Containers: Reopen in Container**.
4. **Follow instructions:** Once the container is ready, follow the instructions in the example's `README.md`. Usually, it's just:
   ```bash
   python main.py
   ```

## 📚 Available Examples

Some examples appear multiple times in the table because they integrate several cloud services.

| Cloud | Service | MVE | Description | Technologies |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | Dynamo DB | [aws-dynamo-db](./src/aws-dynamo-db/) | AWS DynamoDB local development with LocalStack (Terraform/CloudFormation) | DynamoDB, S3, Lambda, Terraform, CloudFormation, LocalStack, Python |
| **AWS** | Dynamo DB | [aws-step-functions](./src/aws-step-functions/) | AWS Step Functions local development with LocalStack | Step Functions, Lambda, DynamoDB, LocalStack, Python |
| **AWS** | Lambda | [aws-dynamo-db](./src/aws-dynamo-db/) | AWS DynamoDB local development with LocalStack (Terraform/CloudFormation) | DynamoDB, S3, Lambda, Terraform, CloudFormation, LocalStack, Python |
| **AWS** | Lambda | [aws-step-functions](./src/aws-step-functions/) | AWS Step Functions local development with LocalStack | Step Functions, Lambda, DynamoDB, LocalStack, Python |
| **AWS** | Lambda | [localstack-docker](./src/localstack-docker/) | LocalStack setup with Lambda and S3 services | LocalStack, Lambda, S3, Docker, Python |
| **AWS** | RDS (Postgres) | [localstack-hybrid-cloud](./src/localstack-hybrid-cloud/) | Hybrid cloud scenario with LocalStack and external Postgres | LocalStack, Terraform, Secrets Manager, PostgreSQL, Docker, Python |
| **AWS** | S3 | [aws-dynamo-db](./src/aws-dynamo-db/) | AWS DynamoDB local development with LocalStack (Terraform/CloudFormation) | DynamoDB, S3, Lambda, Terraform, CloudFormation, LocalStack, Python |
| **AWS** | S3 | [localstack-docker](./src/localstack-docker/) | LocalStack setup with Lambda and S3 services | LocalStack, Lambda, S3, Docker, Python |
| **AWS** | Step Functions | [aws-step-functions](./src/aws-step-functions/) | AWS Step Functions local development with LocalStack | Step Functions, Lambda, DynamoDB, LocalStack, Python |
| **Azure** | Azure Functions | [azure-functions](./src/azure-functions/) | Azure Functions local development with Azurite | Azure Functions, Azurite, Blob Storage, Docker, Python |
| **Azure** | Blob Storage | [azure-functions](./src/azure-functions/) | Azure Functions local development with Azurite | Azure Functions, Azurite, Blob Storage, Docker, Python |
| **Azure** | Blob Storage | [azurite-docker](./src/azurite-docker/) | Azurite setup with Azure Blob Storage emulation | Azurite, Azure, Blob Storage, Docker, Python |
| **Azure** | Cosmos DB | [azure-cosmos-db](./src/azure-cosmos-db/) | Azure Cosmos DB local development with Docker | Cosmos DB, Docker, Python |
| **Azure** | Databricks | [databricks-docker](./src/databricks-docker/) | Local Databricks emulation with Docker, Spark, and Delta Lake | Databricks, Spark, Delta Lake, Docker, Python |
| **GCP** | Cloud Functions | [gcp-functions](./src/gcp-functions/) | Google Cloud Functions local development with Firebase Emulator Suite | Google Cloud Functions, Firebase, Cloud Storage, Python |
| **GCP** | Cloud Run | [gcp-cloud-run](./src/gcp-cloud-run/) | Google Cloud Run local development with Firebase Emulator Suite | Cloud Run, Firebase, Firestore, Docker, Python |
| **GCP** | Cloud Storage | [gcp-functions](./src/gcp-functions/) | Google Cloud Functions local development with Firebase Emulator Suite | Google Cloud Functions, Firebase, Cloud Storage, Python |
| **GCP** | Firestore | [gcp-cloud-run](./src/gcp-cloud-run/) | Google Cloud Run local development with Firebase Emulator Suite | Cloud Run, Firebase, Firestore, Docker, Python |
| **Hybrid** | Airflow | [airflow-docker](./src/airflow-docker/) | Apache Airflow setup with Docker Compose and Python | Apache Airflow, Docker, Python |
| **Hybrid** | Metabase | [metabase-docker](./src/metabase-docker/) | Metabase setup with Docker Compose and PostgreSQL | Metabase, PostgreSQL, Docker, Python |
| **Hybrid** | MinIO | [minio-docker-boto3](./src/minio-docker-boto3/) | MinIO setup with Docker Compose and Boto3 | MinIO, Docker, Boto3, Python |
| **Hybrid** | MinIO | [minio-docker-delta](./src/minio-docker-delta/) | MinIO setup with Docker Compose and Delta Lake | MinIO, Delta Lake, Docker, Python |
| **Hybrid** | Mongo | [mongo-docker-mongoengine](./src/mongo-docker-mongoengine/) | MongoDB setup with Docker Compose and mongoengine ODM | MongoDB, Docker, mongoengine, Python |
| **Hybrid** | Postgres | [localstack-hybrid-cloud](./src/localstack-hybrid-cloud/) | Hybrid cloud scenario with LocalStack and external Postgres | LocalStack, Terraform, Secrets Manager, PostgreSQL, Docker, Python |
| **Hybrid** | Postgres | [postgres-docker-sqlalchemy](./src/postgres-docker-sqlalchemy/) | PostgreSQL setup with Docker Compose and SQLAlchemy ORM | PostgreSQL, Docker, SQLAlchemy, Python |
| **Hybrid** | RabbitMQ | [rabbitmq-docker-pika](./src/rabbitmq-docker-pika/) | RabbitMQ setup with Docker Compose and Python | RabbitMQ, Docker, Python |
| **Hybrid** | Redis | [redis-docker](./src/redis-docker/) | Redis setup with Docker Compose and Python | Redis, Docker, Python |
| **Hybrid** | Redis | [redis-docker-mutex](./src/redis-docker-mutex/) | Distributed mutex using Redis with Docker Compose | Redis, Docker, Python |
| - | Dev Containers | [devcontainers-docker](./src/devcontainers-docker/) | Understanding DevContainers with Python and pandas | DevContainers, Docker, Python, VS Code |

_More examples coming soon..._

## 📝 License

This is a minimal example for educational purposes. Feel free to use and modify as needed.

## 🌐 Follow Me

Connect with me on LinkedIn for more content and updates:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raulcastillabravo/)

---

**Happy coding! 🚀**

If you find these examples helpful, please consider giving this repository a ⭐
