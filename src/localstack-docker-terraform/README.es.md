# Ejemplo de LocalStack + Terraform

Ejemplo mínimo viable para trabajar con LocalStack usando Terraform para el aprovisionamiento de infraestructura. Este ejemplo demuestra cómo crear un entorno completo similar a AWS localmente con S3, Lambda y DynamoDB, todo gestionado a través de Terraform.

## Qué Hace Este Ejemplo

Este ejemplo crea un pipeline de procesamiento de archivos:

1. **Bucket S3**: Recibe archivos subidos (PDF, imágenes, ZIP, etc.)
2. **Función Lambda**: Se activa automáticamente cuando se sube un archivo a S3
3. **Tabla DynamoDB**: Almacena logs con metadatos del archivo (nombre, tamaño, timestamp)

Toda la infraestructura se aprovisiona usando **Terraform** y se ejecuta localmente en **LocalStack**.

## Estructura del Proyecto

```
localstack-docker-terraform/
├── .devcontainer/
│   └── devcontainer.json
├── .vscode/
│   └── settings.json
├── docker-compose.yml
├── .env
├── main.tf                    # Configuración de Terraform
├── lambda_function.py         # Código de la función Lambda
├── package_lambda.py          # Script para empaquetar Lambda
├── main.py                    # Script de demostración
├── pyproject.toml
└── README.md
```

## Requisitos Previos

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (opcional, para configuración con dev container)
- Terraform instalado (incluido automáticamente en Dev Container)

## Opción 1: Usando Dev Container (Recomendado)

### Paso 1: Abrir el Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto
2. Presiona `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Escribe y selecciona: **Dev Containers: Reopen in Container**
4. Espera a que el contenedor se construya y las dependencias se instalen

El Dev Container incluye:
- Python 3.12
- Terraform
- AWS CLI
- Soporte para Docker
- Todas las dependencias de Python

### Paso 2: Iniciar LocalStack

```bash
docker compose up -d
```

Espera unos segundos a que LocalStack esté listo:

```bash
docker compose logs -f
```

Deberías ver: `Ready.`

### Paso 3: Empaquetar la Función Lambda

```bash
python package_lambda.py
```

Esto crea `lambda_function.zip` requerido por Terraform.

### Paso 4: Desplegar la Infraestructura con Terraform

Inicializa Terraform:

```bash
terraform init
```

Aplica la configuración de Terraform:

```bash
terraform apply
```

Escribe `yes` cuando se te solicite. Terraform creará:
- Bucket S3 (`file-uploads-bucket`)
- Tabla DynamoDB (`file-logs`)
- Función Lambda (`s3-file-processor`)
- Roles y políticas IAM
- Notificación de eventos S3

Deberías ver una salida como:

```
Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

bucket_name = "file-uploads-bucket"
dynamodb_table_name = "file-logs"
lambda_function_name = "s3-file-processor"
```

### Paso 5: Ejecutar la Demo

```bash
python main.py
```

Deberías ver una salida como:

```
============================================================
LocalStack + Terraform Demo
S3 → Lambda → DynamoDB Pipeline
============================================================

============================================================
Uploading Sample Files to S3
============================================================

✓ Uploaded: document.pdf (18 bytes)
✓ Uploaded: image.jpg (17 bytes)
✓ Uploaded: archive.zip (18 bytes)
✓ Uploaded: data.json (16 bytes)

============================================================
Waiting for Lambda to process files...
============================================================

============================================================
File Logs from DynamoDB
============================================================

File ID: file-uploads-bucket/data.json
  Name: data.json
  Size: 16 bytes
  Type: application/json
  Uploaded: 2025-12-16T08:36:45.123456

File ID: file-uploads-bucket/archive.zip
  Name: archive.zip
  Size: 18 bytes
  Type: application/zip
  Uploaded: 2025-12-16T08:36:45.098765

...

============================================================
Demo completed successfully!
============================================================
```

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Dependencias

Instalar Terraform:

```bash
# En Ubuntu/Debian
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

Instalar dependencias de Python:

```bash
pip3 install uv && uv sync
```

### Paso 2: Iniciar LocalStack

```bash
docker compose up -d
```

### Paso 3: Empaquetar Lambda y Desplegar con Terraform

```bash
python package_lambda.py
terraform init
terraform apply
```

### Paso 4: Ejecutar la Demo

```bash
python main.py
```

## Componentes del Proyecto

### Configuración de Terraform (`main.tf`)

Define la infraestructura completa:

- **Proveedor AWS**: Configurado para usar endpoints de LocalStack
- **Bucket S3**: `file-uploads-bucket` para almacenamiento de archivos
- **Tabla DynamoDB**: `file-logs` con `file_id` como clave hash
- **Rol IAM**: Para ejecución de Lambda con los permisos necesarios
- **Función Lambda**: Procesa eventos de S3 y registra en DynamoDB
- **Notificación de Eventos S3**: Activa Lambda al subir archivos
- **Outputs**: Muestra los nombres de los recursos creados

### Función Lambda (`lambda_function.py`)

Se activa automáticamente cuando se suben archivos a S3:

- Extrae metadatos del archivo (nombre, tamaño, tipo de contenido)
- Genera timestamp
- Registra la información en la tabla DynamoDB

### Script de Demostración (`main.py`)

Demuestra el flujo completo:

- Sube archivos de ejemplo a S3 (PDF, JPG, ZIP, JSON)
- Espera el procesamiento de Lambda
- Consulta y muestra los logs de DynamoDB

### Script de Empaquetado (`package_lambda.py`)

Crea el paquete ZIP requerido para el despliegue de Lambda:

- Empaqueta `lambda_function.py` en `lambda_function.zip`
- Requerido antes de ejecutar `terraform apply`

## Variables de Entorno

El archivo `.env` contiene:

```
# Credenciales AWS (para LocalStack)
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_DEFAULT_REGION=us-east-1

# Configuración de LocalStack
ENDPOINT_URL=http://localhost:4566

# Configuración de S3
BUCKET_NAME=file-uploads-bucket

# Configuración de DynamoDB
DYNAMODB_TABLE_NAME=file-logs
```

**Nota**: LocalStack acepta cualquier credencial en desarrollo local. Los valores `test/test` son marcadores de posición estándar.

## Comandos Útiles

### Comandos de Docker

```bash
# Iniciar LocalStack
docker compose up -d

# Detener LocalStack
docker compose down

# Ver logs
docker compose logs -f

# Reiniciar LocalStack
docker compose restart
```

### Comandos de Terraform

```bash
# Inicializar Terraform
terraform init

# Planificar cambios
terraform plan

# Aplicar cambios
terraform apply

# Destruir infraestructura
terraform destroy

# Mostrar estado actual
terraform show

# Listar recursos
terraform state list
```

### Comandos de AWS CLI (con LocalStack)

```bash
# Listar buckets S3
aws --endpoint-url=http://localhost:4566 s3 ls

# Listar archivos en bucket
aws --endpoint-url=http://localhost:4566 s3 ls s3://file-uploads-bucket

# Escanear tabla DynamoDB
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name file-logs

# Listar funciones Lambda
aws --endpoint-url=http://localhost:4566 lambda list-functions
```

## Cómo Funciona

1. **Aprovisionamiento de Infraestructura**: Terraform crea todos los recursos AWS en LocalStack
2. **Subida de Archivo**: Cuando se sube un archivo a S3, se genera un evento
3. **Activación de Lambda**: La notificación de eventos S3 activa la función Lambda
4. **Extracción de Metadatos**: Lambda extrae nombre, tamaño y timestamp del archivo
5. **Registro**: Lambda escribe los metadatos en DynamoDB
6. **Consulta**: Puedes consultar DynamoDB para ver todos los logs de archivos

## Solución de Problemas

### Puerto Ya en Uso

Si el puerto 4566 ya está en uso, modifica el `docker-compose.yml`:

```yaml
ports:
  - "4567:4566"
```

Y actualiza `ENDPOINT_URL` en `.env` y `main.tf`.

### Fallo en Terraform Apply

Asegúrate de que LocalStack esté ejecutándose:

```bash
docker ps
```

Deberías ver el contenedor `localstack_terraform_local` ejecutándose.

### Lambda No Se Activa

Verifica los logs de Lambda:

```bash
aws --endpoint-url=http://localhost:4566 logs tail /aws/lambda/s3-file-processor --follow
```

### Paquete Lambda No Encontrado

Asegúrate de ejecutar `package_lambda.py` antes de `terraform apply`:

```bash
python package_lambda.py
```

## Limpieza

Para eliminar todo completamente:

```bash
# Destruir recursos de Terraform
terraform destroy

# Detener y eliminar contenedores
docker compose down -v

# Eliminar paquete Lambda
rm lambda_function.zip

# Eliminar estado de Terraform
rm -rf .terraform terraform.tfstate*
```

## Próximos Pasos

- Añadir más funciones Lambda para diferentes tipos de archivos
- Implementar validación de archivos y manejo de errores
- Añadir notificaciones SNS para resultados de procesamiento
- Crear endpoints de API Gateway
- Añadir métricas y alarmas de CloudWatch
- Implementar Step Functions para flujos de trabajo complejos

## ¿Por Qué Terraform + LocalStack?

- **Infraestructura como Código**: Control de versiones para tu infraestructura
- **Desarrollo Local**: Prueba servicios AWS sin costos en la nube
- **Reproducible**: La misma infraestructura cada vez
- **Iteración Rápida**: Sin esperar el aprovisionamiento en la nube
- **Aprendizaje**: Practica Terraform y servicios AWS de forma segura

## Licencia

Este es un ejemplo mínimo con fines educativos. Siéntete libre de usar y modificar según sea necesario.
