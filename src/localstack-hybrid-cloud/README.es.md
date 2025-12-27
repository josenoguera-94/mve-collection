# Ejemplo de Nube Híbrida con LocalStack

Ejemplo mínimo viable para demostrar un escenario de nube híbrida utilizando LocalStack y una instancia externa de PostgreSQL. Este ejemplo muestra cómo una Lambda de AWS (simulada en LocalStack) puede recuperar secretos de Secrets Manager e interactuar con una base de datos fuera del entorno de AWS.

## Estructura del Proyecto

```
localstack-hybrid-cloud/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── add_user_lambda/          # Código de la función Lambda
│   ├── lambda_handler.py
│   └── models.py
├── docker-compose.yml        # LocalStack + Postgres
├── .env
├── main.py                   # Script de ejecución y verificación
├── main_create_lambda.py     # Script para desplegar la lambda
├── main.tf                   # Infraestructura (Terraform)
├── pyproject.toml
└── README.md
```

## Requisitos Previos

- Docker y Docker Compose instalados
- Terraform instalado
- VS Code con extensión Dev Containers (opcional)

## Pasos de Despliegue

### Paso 1: Levantar la Infraestructura

```bash
docker compose up -d
```

Espera a que los servicios estén listos.

### Paso 2: Inicializar Base de Datos y Secretos

```bash
terraform init
terraform apply -auto-approve
```

### Paso 3: Desplegar la Función Lambda

```bash
pip3 install uv && uv sync
python main_create_lambda.py
```

### Paso 4: Ejecutar el Ejemplo

```bash
python main.py
```

Deberías ver una salida indicando que la Lambda fue invocada y que el usuario fue encontrado correctamente en la base de datos PostgreSQL.

## Componentes del Proyecto

### `main.tf`
Define la infraestructura:
- **AWS Secrets Manager**: Almacena la URI de conexión de Postgres.
- **Provider de PostgreSQL**: Crea la tabla `users` en el contenedor de la base de datos.

### `add_user_lambda/`
Contiene la lógica de la función Lambda:
- `models.py`: Modelos ORM de SQLAlchemy.
- `lambda_handler.py`: Handler que recupera el secreto e inserta un usuario aleatorio.

### `main_create_lambda.py`
Automatiza el proceso de comprimir la carpeta de la lambda y desplegarla en LocalStack usando `boto3`.

## Variables de Entorno

El archivo `.env` contiene:

```
ENDPOINT_URL=http://localhost:4566
AWS_DEFAULT_REGION=us-east-1
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
DATABASE_URL=postgresql://myuser:mypassword@host.docker.internal:5432/mydb
```

## Limpieza

Para eliminar todo:

```bash
terraform destroy -auto-approve
docker compose down -v
```

## Licencia

Este es un ejemplo mínimo para fines educativos. Siéntete libre de usarlo y modificarlo según sea necesario.
