# Minimal Viable Examples (MVE)

A curated collection of minimal, production-ready code examples designed to help developers quickly understand and implement common patterns and technologies.

## 🎯 Objective

This repository provides **clean, minimal, and fully functional examples** that demonstrate specific technologies, patterns, or integrations. Each example is:

- **Self-contained**: Everything you need is included
- **Well-documented**: Clear explanations and step-by-step instructions
- **Container-ready**: Dev Container configuration for consistent development environment
- **Dependency-managed**: Using `uv` for fast and reliable Python dependency management

## 📁 Repository Structure

```
mve-collection/
├── README.md                          # This file
└── src/
    ├── postgres-docker-sqlalchemy/    # Example 1
    │   ├── .devcontainer.json
    │   ├── pyproject.toml
    │   ├── uv.lock
    │   ├── README.md
    │   └── [example files]
    ├── mongo-docker-mongoengine/      # Example 2
    │   ├── .devcontainer.json
    │   ├── pyproject.toml
    │   ├── uv.lock
    │   ├── README.md
    │   └── [example files]
    └── [more examples]/
```

### Structure of Each MVE

Each example follows a consistent structure:

```
src/[mve-name]/
├── .devcontainer.json     # Dev Container configuration
├── pyproject.toml         # Project dependencies (uv)
├── uv.lock               # Locked dependencies
├── README.md             # Example-specific documentation
└── [source files]        # Code and configuration files
```

## 🚀 Quick Start

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed
- [VS Code](https://code.visualstudio.com/) with [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Running an Example

1. **Clone the repository**:

   ```bash
   git clone https://github.com/raulcastillabravo/mve-collection.git
   cd mve-collection
   ```

2. **Open an example in VS Code**:

   ```bash
   cd src/postgres-docker-sqlalchemy
   code .
   ```

3. **Reopen in Dev Container**:

   - Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
   - Select: **Dev Containers: Reopen in Container**
   - Wait for the container to build and dependencies to install

4. **Follow the example's README**:
   - Each example has its own `README.md` with specific instructions

## 📚 Available Examples

| Example                                                         | Description                                               | Technologies                            |
| --------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------- |
| [postgres-docker-sqlalchemy](./src/postgres-docker-sqlalchemy/) | PostgreSQL setup with Docker Compose and SQLAlchemy ORM   | PostgreSQL, Docker, SQLAlchemy, Python  |
| [mongo-docker-mongoengine](./src/mongo-docker-mongoengine/)     | MongoDB setup with Docker Compose and mongoengine ODM     | MongoDB, Docker, mongoengine, Python    |
| [redis-docker](./src/redis-docker/)                             | Redis setup with Docker Compose and Python                | Redis, Docker, Python                   |
| [redis-docker-mutex](./src/redis-docker-mutex/)                 | Distributed mutex using Redis with  Docker Compose        | Redis, Docker, Python                   |
| [rabbitmq-docker-pika](./src/rabbitmq-docker-pika/)             | RabbitMQ setup with Docker Compose and Python             | RabbitMQ, Docker, Python                |
| [airflow-docker](./src/airflow-docker/)                         | Apache Airflow setup with Docker Compose and Python       | Apache Airflow, Docker, Python          |
| [minio-docker-boto3](./src/minio-docker-boto3/)                 | MinIO setup with Docker Compose and Boto3                 | MinIO, Docker, Boto3, Python            |
| [minio-docker-delta](./src/minio-docker-delta/)                 | MinIO setup with Docker Compose and Delta Lake            | MinIO, Delta Lake, Docker, Python       |
| [metabase-docker](./src/metabase-docker/)                       | Metabase setup with Docker Compose and PostgreSQL         | Metabase, PostgreSQL, Docker, Python    |
| [localstack-docker](./src/localstack-docker/)                   | LocalStack setup with Lambda and S3 services              | LocalStack, Lambda, S3, Docker, Python  |
| [azurite-docker](./src/azurite-docker/)                         | Azurite setup with Azure Blob Storage emulation           | Azurite, Azure, Blob Storage, Docker, Python |
| _More examples coming soon..._                                  |                                                           |                                         |

## 🛠️ Technology Stack

### Core Technologies

- **Python 3.12+**: Primary programming language
- **uv**: Fast Python package installer and resolver
- **Docker**: Containerization and service orchestration
- **Dev Containers**: Consistent development environments

### Example-Specific Technologies

Each example may include additional technologies like:

- Databases (PostgreSQL, MongoDB, Redis)
- Web frameworks (FastAPI, Flask, Django)
- Message queues (RabbitMQ, Kafka)
- And more...

## 🤝 Contributing

Contributions are welcome! If you have a minimal viable example you'd like to share:

1. Fork the repository
2. Create a new directory under `src/` with your example name
3. Follow the standard structure (see above)
4. Include a comprehensive `README.md`
5. Test your example in the Dev Container
6. Submit a pull request

### Guidelines for New Examples

- **Keep it minimal**: Only include what's necessary to demonstrate the concept
- **Document thoroughly**: Clear explanations and commands
- **Use uv**: Manage dependencies with `pyproject.toml` and `uv.lock`
- **Include Dev Container**: Provide `.devcontainer.json` for easy setup
- **Follow best practices**: Proper error handling, environment variables, etc.

## 📖 Why This Repository?

Learning new technologies often involves:

- ❌ Wading through extensive documentation
- ❌ Debugging complex setup issues
- ❌ Finding outdated examples
- ❌ Missing dependencies or configurations

This repository solves these problems by providing:

- ✅ Ready-to-run examples
- ✅ Containerized environments
- ✅ Complete dependency specifications
- ✅ Clear, step-by-step documentation
- ✅ Best practices and patterns

## 📝 License

This repository is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

Each example credits the technologies and resources that made it possible. See individual example READMEs for specific attributions.

## 🌐 Follow Me

Connect with me on LinkedIn for more content and updates:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raulcastillabravo/)

---

**Happy coding! 🚀**

If you find these examples helpful, please consider giving this repository a ⭐
