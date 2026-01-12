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
- [AWS CLI](https://aws.amazon.com/cli/) (Incluido en el Dev Container)

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

### Paso 4: Esperar la inicialización de la Lambda

Espera **5-10 segundos** para que LocalStack termine de inicializar el entorno de la Lambda.

### Paso 5: Ejecutar el Flujo de Trabajo

```bash
python main.py
```

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Dependencias

```bash
pip3 install uv && uv sync
```

Instala manualmente el **AWS Toolkit** desde el Marketplace de VS Code.

### Paso 3: Instalar AWS CLI

Si no lo tienes, instala el [AWS CLI](https://aws.amazon.com/cli/).

### Paso 4: Ejecutar el Ejemplo

Sigue los mismos pasos que en el Dev Container (Levantar LocalStack, Desplegar, Ejecutar).

---

## Configurar Perfil de LocalStack

Antes de ejecutar el ejemplo, configura un perfil de AWS dedicado para LocalStack. Esto asegura que tanto la CLI como el AWS Toolkit apunten a tu entorno local:

```bash
aws configure set aws_access_key_id test --profile localstack
aws configure set aws_secret_access_key test --profile localstack
aws configure set region us-east-1 --profile localstack
aws configure set output json --profile localstack
aws configure set endpoint_url http://localhost:4566 --profile localstack
```

> **Nota**: Este perfil redirigirá todo el tráfico a `localhost:4566`.

## Pasos de Validación

Después de ejecutar `main.py`, puedes verificar que todos los recursos se crearon y poblaron correctamente usando AWS CLI:

### 1. Verificar Creación de Usuario IAM
Comprueba si el usuario IAM fue creado por la Step Function (IAM no es visible en el AWS Explorer del Toolkit):
```bash
aws iam list-users --profile localstack
```

### 2. Verificar Logs en DynamoDB
Revisa las entradas en la tabla `UserLogs`:
```bash
aws dynamodb scan --table-name UserLogs --profile localstack
```

### 3. Verificar Funciones Lambda
Lista las funciones desplegadas:
```bash
aws lambda list-functions --profile localstack
```

---

## Trabajando con el AWS Toolkit (Editor de Step Functions)

Este MVE está diseñado para aprovechar el editor ASL que proporciona el AWS Toolkit.

### 1. Ver/Editar la Step Function

1. Abre `step_function.asl.json`.
2. Haz clic en el icono **"Render Graph"** (esquina superior derecha del editor) para ver una representación visual del flujo.
3. Puedes modificar los estados y el gráfico se actualizará en tiempo real.

### 2. Ejecución y Debugging

LocalStack soporta la ejecución de Step Functions. Aunque el AWS Toolkit suele conectarse a una cuenta real de AWS, puedes usar `main.py` para lanzar ejecuciones localmente y ver los logs en la terminal.

#### Depuración de Funciones Lambda por Separado
Para aislar problemas, puedes invocar las Lambdas de forma independiente usando la CLI:

**Probar Validación de Email:**
```bash
aws lambda invoke \
  --function-name ValidateEmailLambda \
  --payload '{"email": "valid@example.com"}' \
  --cli-binary-format raw-in-base64-out \
  --profile localstack \
  response.json
```

**Probar Registro de Usuario:**
```bash
aws lambda invoke \
  --function-name LogUserLambda \
  --payload '{"username": "debug_user", "email": "debug@example.com"}' \
  --cli-binary-format raw-in-base64-out \
  --profile localstack \
  response.json
```

Si una Lambda falla, revisa los logs de LocalStack: `docker compose logs -f localstack`.

### 3. Visualización y Ejecución desde VS Code

El **AWS Toolkit** te permite renderizar el grafo del flujo de trabajo y disparar ejecuciones directamente desde el IDE:

1.  **Abrir Paleta de Comandos**: Presiona `F1` o `Ctrl+Shift+P`.
2.  **Conectar a AWS**: Escribe y selecciona **AWS: Connect to AWS**.
3.  **Seleccionar Perfil**: Elige el perfil `localstack` que creaste en el primer paso.
4.  **Explorar**: En la barra lateral del **AWS Explorer**, ahora deberías ver los servicios emulados.
5.  **Renderizar Grafo**:
    *   Abre `step_function.asl.json`.
    *   Haz clic en el icono de **Visual Graph** (arriba a la derecha del editor) para ver la lógica.
6.  **Ejecutar**:
    *   En el **AWS Explorer**, despliega **Step Functions** y busca `UserOnboardingWorkflow`.
    *   Haz clic derecho y selecciona **Start Execution** para dispararlo.

> **Nota**: Aunque el IDE permite lanzar ejecuciones y ver el grafo ASL, el seguimiento del estado de la ejecución se realiza a través de la salida de terminal de `main.py` o inspeccionando los logs de LocalStack.

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

## Resolución de Problemas

### La función Lambda está en estado 'Pending'

Si ejecutas `main.py` inmediatamente después de `deploy.py`, podrías ver este error:
`The operation cannot be performed at this time. The function is currently in the following state: Pending`

**Solución**: Espera de 5 a 10 segundos para que LocalStack termine de inicializar el entorno de la Lambda y vuelve a ejecutar `main.py`.

## Limpieza

Para eliminar completamente todo:

```bash
docker compose down -v
```

## Licencia

Este es un ejemplo mínimo para fines educativos. Siéntete libre de usarlo y modificarlo según necesites.
