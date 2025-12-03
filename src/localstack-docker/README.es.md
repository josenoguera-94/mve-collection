# Ejemplo de LocalStack + Lambda + S3

Ejemplo mínimo viable para trabajar con servicios de AWS localmente usando LocalStack, Docker Compose y Python. Este ejemplo demuestra cómo crear y desplegar una función Lambda que sube objetos a S3.

## Estructura del Proyecto

```
localstack-docker/
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── .env
├── deploy.py
├── lambda_s3_uploader.py
├── main_create_lambda.py
├── main_run_lambda.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prerrequisitos

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (opcional, para configuración con dev container)

## Opción 1: Usando Dev Container (Recomendado)

### Paso 1: Abrir el Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto
2. Presiona `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Escribe y selecciona: **Dev Containers: Reopen in Container**
4. Espera a que el contenedor se construya y se instalen las dependencias

### Paso 2: Iniciar el Contenedor de LocalStack

Dentro de la terminal del dev container:

```bash
docker compose up -d
```

Verifica que esté ejecutándose:

```bash
docker ps
```

### Paso 3: Crear la Función Lambda y el Bucket S3

Ejecuta el script de creación:

```bash
python main_create_lambda.py
```

Deberías ver una salida como:

```
Connecting to LocalStack at http://localhost:4566...
Creating bucket 'test-bucket'...
Creating UploadToS3.zip...
Lambda function 'UploadToS3' deployed successfully!
You can now verify the function exists using AWS CLI.
```

### Paso 4: Verificar que la Función Lambda Existe

El dev container incluye AWS CLI preinstalado. Primero, configura las credenciales de AWS (LocalStack acepta cualquier valor ficticio):

```bash
aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set region us-east-1
aws configure set output json
```

Luego verifica que la función Lambda fue creada:

```bash
aws --endpoint-url=http://localhost:4566 lambda list-functions
```

O obtén detalles sobre la función específica:

```bash
aws --endpoint-url=http://localhost:4566 lambda get-function --function-name UploadToS3
```

Deberías ver los detalles de la función incluyendo su estado, runtime y handler.

**Alternativa: Usando un Script de Python**

Si prefieres, puedes verificar usando Python:

```python
import boto3
import os
from dotenv import load_dotenv

load_dotenv()
lambda_client = boto3.client('lambda', 
    endpoint_url=os.getenv("ENDPOINT_URL", "http://localhost:4566"),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"))

response = lambda_client.list_functions()
for func in response['Functions']:
    print(f"Function: {func['FunctionName']}, Runtime: {func['Runtime']}, State: {func['State']}")
```

### Paso 5: Ejecutar la Función Lambda

Ahora ejecuta la función Lambda:

```bash
python main_run_lambda.py
```

Deberías ver una salida como:

```
Connecting to LocalStack at http://localhost:4566...
Invoking Lambda function 'UploadToS3'...
Lambda response: {'statusCode': 200, 'body': 'Successfully uploaded hello.txt to test-bucket'}
Verifying S3 upload...
Content from S3: Hello from Lambda!
```

### Paso 6: Verificar el Objeto en S3 Usando AWS CLI

También puedes verificar que el objeto en S3 fue creado usando AWS CLI:

**Listar objetos en el bucket:**

```bash
aws --endpoint-url=http://localhost:4566 s3 ls s3://test-bucket/
```

Deberías ver `hello.txt` en la salida.

**Leer el contenido del objeto:**

```bash
aws --endpoint-url=http://localhost:4566 s3 cp s3://test-bucket/hello.txt -
```

Esto mostrará el contenido: `Hello from Lambda!`

**Obtener metadatos del objeto:**

```bash
aws --endpoint-url=http://localhost:4566 s3api head-object --bucket test-bucket --key hello.txt
```

Esto muestra metadatos como tamaño, fecha de última modificación, etc.

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Dependencias de Python

```bash
pip3 install uv && uv sync
```

### Paso 2: Iniciar el Contenedor de LocalStack

```bash
docker compose up -d
```

### Paso 3: Crear la Función Lambda

```bash
python main_create_lambda.py
```

### Paso 4: Verificar la Función Lambda

Si no tienes AWS CLI instalado localmente, instálalo:

```bash
pip install awscli
```

Configura las credenciales de AWS:

```bash
aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set region us-east-1
aws configure set output json
```

Luego verifica la función Lambda:

```bash
aws --endpoint-url=http://localhost:4566 lambda list-functions
```

### Paso 5: Ejecutar la Función Lambda

```bash
python main_run_lambda.py
```

## Componentes del Proyecto

### LambdaDeployer (`deploy.py`)

Clase para desplegar funciones Lambda en LocalStack:

- **Constructor**: Lee las variables de entorno (`ENDPOINT_URL`, `AWS_DEFAULT_REGION`, `LAMBDA_INTERNAL_ENDPOINT`) y crea el cliente Lambda
- **`deploy(lambda_file_path, dependencies, function_name)`**: Despliega una función Lambda
  - Crea un archivo zip con la función y sus dependencias
  - Elimina cualquier función existente con el mismo nombre
  - Crea la nueva función Lambda
  - Limpia archivos temporales
- **Métodos privados**: `_create_zip()`, `_delete_lambda()`, `_remove_zip()` manejan operaciones internas

### Función Lambda (`lambda_s3_uploader.py`)

Función Lambda simple que sube objetos a S3:

- **`lambda_handler(event, context)`**: Punto de entrada principal para la función Lambda
  - Recibe `bucket_name`, `key` y `body` en el evento
  - Usa boto3 para subir el objeto a S3
  - Retorna una respuesta de éxito

Esta es una función independiente sin herencia ni dependencias de clases personalizadas.

### Scripts Principales

**`main_create_lambda.py`**: 
- Crea el bucket S3 usando boto3 (si no existe)
- Usa `LambdaDeployer` para desplegar la función Lambda en LocalStack

**`main_run_lambda.py`**:
- Usa boto3 para invocar la función Lambda con un payload
- Verifica que el archivo fue subido a S3 usando boto3 directamente

## Variables de Entorno

El archivo `.env` contiene:

```
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_DEFAULT_REGION=us-east-1
ENDPOINT_URL=http://localhost:4566
LAMBDA_INTERNAL_ENDPOINT=http://localstack:4566
BUCKET_NAME=test-bucket
```

## Comandos Útiles

### Comandos de Docker

```bash
# Iniciar contenedores
docker compose up -d

# Detener contenedores
docker compose down

# Detener y eliminar volúmenes (eliminar todos los datos)
docker compose down -v

# Ver logs
docker compose logs -f

# Ver solo logs de LocalStack
docker compose logs -f localstack
```

## Solución de Problemas

### Puerto Ya en Uso

Si el puerto 4566 ya está en uso, modifica la sección de puertos en `docker-compose.yml`:

```yaml
ports:
  - "4567:4566"
```

Luego actualiza `ENDPOINT_URL` en `.env`:

```
ENDPOINT_URL=http://localhost:4567
```

Y reinicia:

```bash
docker compose down
docker compose up -d
```

### Conexión Rechazada

Asegúrate de que el contenedor de LocalStack esté ejecutándose:

```bash
docker ps
```

Verifica los logs en busca de errores:

```bash
docker compose logs localstack
```

### Módulo No Encontrado

Si obtienes errores de importación, instala las dependencias:

```bash
pip3 install uv && uv sync
```

## Limpieza

Para eliminar todo completamente:

```bash
# Detener y eliminar contenedores y volúmenes
docker compose down -v

# Eliminar la imagen de LocalStack (opcional)
docker rmi localstack/localstack
```

## Próximos Pasos

- Agregar más funciones Lambda para diferentes operaciones
- Implementar integración con API Gateway
- Agregar ejemplos de DynamoDB
- Implementar patrones de mensajería SNS/SQS
- Agregar pruebas unitarias para funciones Lambda

## Licencia

Este es un ejemplo mínimo con fines educativos. Siéntete libre de usar y modificar según sea necesario.
