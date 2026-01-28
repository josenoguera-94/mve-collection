# Ejemplos Mínimos Viables (MVE)

Una colección curada de ejemplos de código mínimos y listos para producción, diseñados para ayudar a los desarrolladores a comprender e implementar rápidamente patrones y tecnologías comunes.

## 🎯 Objetivo

Este repositorio proporciona **ejemplos limpios, mínimos y completamente funcionales** que demuestran tecnologías, patrones o integraciones específicas. Cada ejemplo es:

- **Autocontenido**: Todo lo que necesitas está incluido
- **Bien documentado**: Explicaciones claras e instrucciones paso a paso
- **Listo para contenedores**: Configuración de Dev Container para un entorno de desarrollo consistente
- **Gestión de dependencias**: Usando `uv` para una gestión rápida y confiable de dependencias de Python

## 📁 Estructura del Repositorio

```
mve-collection/
├── README.md                          # Este archivo
└── src/
    ├── postgres-docker-sqlalchemy/    # Ejemplo 1
    │   ├── .devcontainer.json
    │   ├── pyproject.toml
    │   ├── uv.lock
    │   ├── README.md
    │   └── [archivos del ejemplo]
    ├── mongo-docker-mongoengine/      # Ejemplo 2
    │   ├── .devcontainer.json
    │   ├── pyproject.toml
    │   ├── uv.lock
    │   ├── README.md
    │   └── [archivos del ejemplo]
    └── [más ejemplos]/
```

### Estructura de Cada MVE

Cada ejemplo sigue una estructura consistente:

```
src/[nombre-mve]/
├── .devcontainer.json     # Configuración de Dev Container
├── pyproject.toml         # Dependencias del proyecto (uv)
├── uv.lock               # Dependencias bloqueadas
├── README.md             # Documentación específica del ejemplo
└── [archivos fuente]     # Archivos de código y configuración
```

## 🚀 Inicio Rápido

### Requisitos Previos

- [Docker](https://www.docker.com/get-started) instalado
- [VS Code](https://code.visualstudio.com/) con la extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Ejecutar un Ejemplo

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/raulcastillabravo/mve-collection.git
   cd mve-collection
   ```

2. **Abrir un ejemplo en VS Code**:

   ```bash
   cd src/postgres-docker-sqlalchemy
   code .
   ```

3. **Reabrir en Dev Container**:

   - Presiona `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
   - Selecciona: **Dev Containers: Reopen in Container**
   - Espera a que el contenedor se construya y las dependencias se instalen

4. **Seguir el README del ejemplo**:
   - Cada ejemplo tiene su propio `README.md` con instrucciones específicas

## 📚 Ejemplos Disponibles

| Ejemplo                                                         | Descripción                                                     | Tecnologías                              |
| --------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------- |
| [airflow-docker](./src/airflow-docker/)                         | Configuración de Apache Airflow con Docker Compose y Python     | Apache Airflow, Docker, Python           |
| [aws-dynamo-db](./src/aws-dynamo-db/) | Desarrollo local de AWS DynamoDB con LocalStack (Terraform/CloudFormation) | DynamoDB, S3, Lambda, Terraform, CloudFormation, LocalStack, Python |
| [aws-step-functions](./src/aws-step-functions/)           | Desarrollo local de AWS Step Functions con LocalStack      | Step Functions, Lambda, DynamoDB, LocalStack, Python |
| [azure-cosmos-db](./src/azure-cosmos-db/) | Desarrollo local de Azure Cosmos DB con Docker | Cosmos DB, Docker, Python |
| [azure-functions](./src/azure-functions/)                       | Desarrollo local de Azure Functions con Azurite                 | Azure Functions, Azurite, Blob Storage, Docker, Python |
| [azurite-docker](./src/azurite-docker/)                         | Configuración de Azurite con emulación de Azure Blob Storage    | Azurite, Azure, Blob Storage, Docker, Python |
| [databricks-docker](./src/databricks-docker/)                       | Emulación local de Databricks con Docker, Spark y Delta Lake | Databricks, Spark, Delta Lake, Docker, Python |
| [devcontainers-docker](./src/devcontainers-docker/)             | Entendiendo DevContainers con Python y pandas                   | DevContainers, Docker, Python, VS Code   |
| [gcp-cloud-run](./src/gcp-cloud-run/)               | Desarrollo local de Google Cloud Run con Firebase Emulator Suite | Cloud Run, Firebase, Firestore, Docker, Python |
| [gcp-functions](./src/gcp-functions/)                           | Desarrollo local de Google Cloud Functions con Firebase Emulator Suite | Google Cloud Functions, Firebase, Cloud Storage, Python |
| [localstack-docker](./src/localstack-docker/)                   | Configuración de LocalStack con servicios Lambda y S3           | LocalStack, Lambda, S3, Docker, Python   |
| [localstack-docker](./src/localstack-docker/)                   | Configuración de LocalStack con servicios Lambda y S3           | LocalStack, Lambda, S3, Docker, Python   |
| [localstack-hybrid-cloud](./src/localstack-hybrid-cloud/) | Escenario de nube híbrida con LocalStack y Postgres externo | LocalStack, Terraform, Secrets Manager, PostgreSQL, Docker, Python |
| [metabase-docker](./src/metabase-docker/)                       | Configuración de Metabase con Docker Compose y PostgreSQL       | Metabase, PostgreSQL, Docker, Python     |
| [minio-docker-boto3](./src/minio-docker-boto3/)                 | Configuración de MinIO con Docker Compose y Boto3               | MinIO, Docker, Boto3, Python             |
| [minio-docker-delta](./src/minio-docker-delta/)                 | Configuración de MinIO con Docker Compose y Delta Lake          | MinIO, Delta Lake, Docker, Python        |
| [mongo-docker-mongoengine](./src/mongo-docker-mongoengine/)     | Configuración de MongoDB con Docker Compose y ODM mongoengine   | MongoDB, Docker, mongoengine, Python     |
| [postgres-docker-sqlalchemy](./src/postgres-docker-sqlalchemy/) | Configuración de PostgreSQL con Docker Compose y ORM SQLAlchemy | PostgreSQL, Docker, SQLAlchemy, Python   |
| [rabbitmq-docker-pika](./src/rabbitmq-docker-pika/)             | Configuración de RabbitMQ con Docker Compose y Python           | RabbitMQ, Docker, Python                 |
| [redis-docker](./src/redis-docker/)                             | Configuración de Redis con Docker Compose y Python              | Redis, Docker, Python                    |
| [redis-docker-mutex](./src/redis-docker-mutex/)                 | Mutex distribuido usando Redis con Docker Compose               | Redis, Docker, Python                    |
| _Más ejemplos próximamente..._                                  |                                                                 |                                          |

## 🛠️ Stack Tecnológico

### Tecnologías Core

- **Python 3.14+**: Lenguaje de programación principal
- **uv**: Instalador y resolvedor rápido de paquetes de Python
- **Docker**: Contenedorización y orquestación de servicios
- **Dev Containers**: Entornos de desarrollo consistentes

### Tecnologías Específicas por Ejemplo

Cada ejemplo puede incluir tecnologías adicionales como:

- Bases de datos (PostgreSQL, MongoDB, Redis)
- Frameworks web (FastAPI, Flask, Django)
- Colas de mensajes (RabbitMQ, Kafka)
- Y más...

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si tienes un ejemplo mínimo viable que te gustaría compartir:

1. Haz un fork del repositorio
2. Crea un nuevo directorio bajo `src/` con el nombre de tu ejemplo
3. Sigue la estructura estándar (ver arriba)
4. Incluye un `README.md` completo
5. Prueba tu ejemplo en el Dev Container
6. Envía un pull request

### Directrices para Nuevos Ejemplos

- **Mantenlo mínimo**: Solo incluye lo necesario para demostrar el concepto
- **Documenta exhaustivamente**: Explicaciones claras y comandos
- **Usa uv**: Gestiona las dependencias con `pyproject.toml` y `uv.lock`
- **Incluye Dev Container**: Proporciona `.devcontainer.json` para configuración fácil
- **Sigue las mejores prácticas**: Manejo adecuado de errores, variables de entorno, etc.

## 📖 ¿Por Qué Este Repositorio?

Aprender nuevas tecnologías a menudo implica:

- ❌ Navegar por documentación extensa
- ❌ Depurar problemas complejos de configuración
- ❌ Encontrar ejemplos desactualizados
- ❌ Dependencias o configuraciones faltantes

Este repositorio resuelve estos problemas proporcionando:

- ✅ Ejemplos listos para ejecutar
- ✅ Entornos contenedorizados
- ✅ Especificaciones completas de dependencias
- ✅ Documentación clara paso a paso
- ✅ Mejores prácticas y patrones

## 📝 Licencia

Este repositorio es de código abierto y está disponible bajo la [Licencia MIT](LICENSE).

## 🙏 Agradecimientos

Cada ejemplo acredita las tecnologías y recursos que lo hicieron posible. Consulta los READMEs individuales de cada ejemplo para atribuciones específicas.

## 🌐 Sígueme

Conéctate conmigo en LinkedIn para más contenido y actualizaciones:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raulcastillabravo/)

---

**¡Feliz programación! 🚀**

Si encuentras estos ejemplos útiles, por favor considera darle una ⭐ a este repositorio
