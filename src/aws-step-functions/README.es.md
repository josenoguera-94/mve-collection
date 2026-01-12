# Desarrollo Local de AWS Step Functions

Ejemplo mínimo viable para trabajar con **AWS Step Functions** de forma local utilizando **LocalStack** y el **AWS Toolkit de VS Code**. Este ejemplo demuestra un flujo de alta de usuario con ejecución paralela de Lambdas y creación de un usuario de IAM.

## Estructura del Proyecto

```
aws-step-functions/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── lambdas/
│   ├── log_user.py          # Escribe en DynamoDB
│   └── validate_email.py    # Valida el formato del email
├── deploy.py                # Script de despliegue de infraestructura
├── docker-compose.yml       # Servicios de LocalStack
├── main.py                  # Script de ejecución del flujo
├── pyproject.toml
├── step_function.asl.json   # Definición de la Step Function (ASL)
├── utils.py                 # Utilidades para ZIP y configuración
└── README.md
```

## Prerrequisitos

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (Recomendado)
- [AWS Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-aws-us.aws-toolkit-vscode) (Incluido en el Dev Container)

## Opción 1: Usando Dev Container (Recomendado)

### Paso 1: Abrir el Proyecto en el Dev Container

1. Abre VS Code en la carpeta del proyecto.
2. Presiona `F1` y selecciona: **Dev Containers: Reopen in Container**.
3. Espera a que finalice la construcción.

### Paso 2: Levantar LocalStack

```bash
docker compose up -d
```

### Paso 3: Desplegar la Infraestructura

```bash
python deploy.py
```

### Paso 4: Ejecutar el Flujo de Trabajo

```bash
python main.py
```

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Dependencias

```bash
pip3 install uv && uv sync
```

### Paso 2: Instalar AWS Toolkit

Instala manualmente el **AWS Toolkit** desde el Marketplace de VS Code.

### Paso 3: Ejecutar el Ejemplo

Sigue los mismos pasos que en el Dev Container (Levantar LocalStack, Desplegar, Ejecutar).

---

## Trabajando con el AWS Toolkit (Editor de Step Functions)

Este MVE está diseñado para aprovechar el editor ASL que proporciona el AWS Toolkit.

### 1. Ver/Editar la Step Function

1. Abre `step_function.asl.json`.
2. Haz clic en el icono **"Render Graph"** (esquina superior derecha del editor) para ver una representación visual del flujo.
3. Puedes modificar los estados y el gráfico se actualizará en tiempo real.

### 2. Ejecución y Debugging

LocalStack soporta la ejecución de Step Functions. Aunque el AWS Toolkit suele conectarse a una cuenta real de AWS, puedes usar `main.py` para lanzar ejecuciones localmente y ver los logs en la terminal.

Para depurar un estado específico:
1. Modifica el input en `main.py`.
2. Revisa los logs de LocalStack: `docker compose logs -f localstack`.

## Componentes del Proyecto

### Lambdas (`lambdas/`)

- **LogUserLambda**: Guarda los datos del usuario y la fecha en una tabla de DynamoDB llamada `UserLogs`.
- **ValidateEmailLambda**: Valida si el email proporcionado cumple con un formato regex estándar.

### Step Function (`step_function.asl.json`)

- **ProcessUserOnboarding**: Un estado tipo `Parallel` que lanza ambas Lambdas simultáneamente.
- **CreateIAMUser**: Un `Task` que utiliza la integración directa con el SDK de AWS para crear un usuario de IAM local si los pasos anteriores tienen éxito.

## Variables de Entorno

El archivo `.env` contiene:

```
AWS_REGION=us-east-1
LOCALSTACK_ENDPOINT=http://localhost:4566
DYNAMODB_TABLE=UserLogs
STEP_FUNCTION_NAME=UserOnboardingWorkflow
```

## Licencia

Este es un ejemplo mínimo para fines educativos. Siéntete libre de usarlo y modificarlo según necesites.
