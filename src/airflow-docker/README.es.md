# Airflow + Docker ETL Pipeline Example

Ejemplo mínimo viable para Apache Airflow con Docker, demostrando un pipeline ETL (Extract, Transform, Load) simple usando Python y pandas con almacenamiento basado en archivos.

## Estructura del Proyecto

```
airflow-etl-pipeline/
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── .env
├── dags/
│   ├── dag.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── storage/
│   ├── extract/
│   ├── transform/
│   └── load/
├── logs/
├── plugins/
├── pyproject.toml
├── uv.lock
├── README.md
└── README.es.md
```

## Requisitos Previos

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (opcional, para usar dev container)
- Navegador web para acceder a la interfaz de Airflow

## Opción 1: Usando Dev Container (Recomendado)

### Paso 1: Abrir Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto
2. Presiona `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Escribe y selecciona: **Dev Containers: Reopen in Container**
4. Espera a que el contenedor se construya y las dependencias se instalen

### Paso 2: Crear Directorios Requeridos

Dentro del terminal del dev container:

```bash
mkdir -p dags logs plugins storage/extract storage/transform storage/load
```

### Paso 3: Copiar Archivos del DAG

Copia los archivos del pipeline ETL al directorio `dags`:

```bash
cp extract.py transform.py load.py dag.py dags/
```

### Paso 4: Iniciar Airflow

Inicia todos los servicios de Airflow:

```bash
docker-compose up -d
```

Espera a que todos los servicios estén saludables (puede tomar 1-2 minutos):

```bash
docker-compose ps
```

Deberías ver todos los servicios ejecutándose:

- `airflow_postgres`
- `airflow_webserver`
- `airflow_scheduler`

### Paso 5: Acceder a la Interfaz de Airflow

Abre tu navegador web y navega a:

```
http://localhost:8080
```

Inicia sesión con las credenciales por defecto:

- **Usuario:** `admin`
- **Contraseña:** `admin`

### Paso 6: Habilitar el DAG

1. En la interfaz de Airflow, deberías ver el DAG `etl_pipeline`
2. Haz clic en el interruptor para habilitar el DAG (se volverá verde/azul)
3. El DAG está programado para ejecutarse automáticamente cada 30 segundos

### Paso 7: Monitorizar la Ejecución

1. Haz clic en el nombre del DAG para ver sus detalles
2. Verás la vista de Grafo mostrando las tres tareas:
   - `extract_task` → `transform_task` → `load_task`
3. Observa cómo las tareas se ejecutan automáticamente cada 30 segundos
4. Cada tarea cambiará de blanco → verde claro → verde oscuro (completada)

### Paso 8: Ver Logs

Para ver los logs detallados de cada tarea:

1. Haz clic en una caja de tarea (ej., `extract_task`)
2. Haz clic en la instancia de tarea (fecha/hora)
3. Haz clic en el botón "Log"
4. Verás la salida de cada paso de ETL

Salida esperada en los logs:

**Tarea Extract:**

```
Starting data extraction...
✓ Extracted 5 rows
✓ Saved to: storage/extract/data_20240115_143052.csv

Extracted data:
   id  value category
0   1     42        A
1   2     73        B
2   3     15        C
3   4     88        A
4   5     51        B
```

**Tarea Transform:**

```
Starting data transformation...
Reading from: storage/extract/data_20240115_143052.csv

Data before transformation:
   id  value category
0   1     42        A
1   2     73        B
2   3     15        C
3   4     88        A
4   5     51        B

✓ Transformed 5 rows
✓ Saved to: storage/transform/data_20240115_143052.csv

Data after transformation:
   id  value category
0   1     84        A
1   2    146        B
2   3     30        C
3   4    176        A
4   5    102        B
```

**Tarea Load:**

```
Starting data loading...
Reading from: storage/transform/data_20240115_143052.csv

Data to be loaded:
   id  value category
0   1     84        A
1   2    146        B
2   3     30        C
3   4    176        A
4   5    102        B

✓ Inserted 5 rows into database
✓ Saved to: storage/load/data_20240115_143052.csv
```

### Paso 9: Verificar Archivos Generados

Revisa los directorios de storage para ver los archivos CSV generados:

```bash
ls -la storage/extract/
ls -la storage/transform/
ls -la storage/load/
```

Cada ejecución crea archivos con timestamps como `data_20240115_143052.csv`.

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Dependencias con uv

```bash
pip install uv && uv sync
```

### Paso 2: Crear Directorios Requeridos y Copiar Archivos

```bash
mkdir -p dags logs plugins storage/extract storage/transform storage/load
cp extract.py transform.py load.py dag.py dags/
```

### Paso 3: Iniciar Airflow

```bash
docker-compose up -d
```

### Paso 4: Acceder y Usar Airflow

Sigue los pasos 5-9 de la Opción 1.

## Explicación del Pipeline ETL

### Extract (extract.py)

- **Clase:** `Extract`
- **Método:** `run()`
- Crea un DataFrame de pandas con 5 filas y 3 columnas
- Columnas: `id`, `value`, `category`
- Los valores se generan aleatoriamente
- Guarda los datos en `storage/extract/data_[timestamp].csv`
- Devuelve la ruta del archivo

### Transform (transform.py)

- **Clase:** `Transform`
- **Método:** `run(input_path)`
- Lee el CSV del directorio extract
- Duplica los valores en la columna `value`
- Guarda los datos transformados en `storage/transform/data_[timestamp].csv`
- Devuelve la ruta del archivo de salida

### Load (load.py)

- **Clase:** `Load`
- **Método:** `run(input_path)`
- Lee el CSV del directorio transform
- Simula una inserción en base de datos
- Guarda los datos en `storage/load/data_[timestamp].csv`
- Devuelve el número de filas cargadas

### DAG (dag.py)

- Usa el decorador `@dag` para definir el flujo de trabajo
- Usa el decorador `@task` para cada paso de ETL
- Se ejecuta cada 30 segundos (`schedule_interval=timedelta(seconds=30)`)
- Las tareas están encadenadas: `extract_task >> transform_task >> load_task`
- Cada tarea pasa la ruta del archivo a la siguiente tarea

## Conceptos de Airflow

### DAG (Directed Acyclic Graph)

Una colección de tareas con dependencias, representando un flujo de trabajo.

### Decorador de Tarea (@task)

Forma moderna de definir tareas en Airflow usando funciones de Python.

### Dependencias de Tareas

El operador `>>` define el orden de ejecución: `tarea1 >> tarea2` significa que tarea2 se ejecuta después de tarea1.

### Context Manager (with)

El decorador `@dag` crea un DAG usando el patrón de context manager de Python.

### XCom (Cross-Communication)

Los valores de retorno de las tareas se almacenan automáticamente en XCom y se pasan a las tareas dependientes.

### Scheduler

Monitoriza los DAGs y activa la ejecución de tareas según la programación (cada 30 segundos en este ejemplo).

### Webserver

Proporciona la interfaz web para monitorizar y gestionar DAGs.

## Variables de Entorno

El archivo `.env` contiene:

```
AIRFLOW_USER=admin
AIRFLOW_PASSWORD=admin
```

## Comandos Útiles

### Comandos de Docker

```bash
# Iniciar todos los servicios
docker-compose up -d

# Detener todos los servicios
docker-compose down

# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f airflow-webserver

# Reiniciar servicios
docker-compose restart

# Detener y eliminar todos los datos
docker-compose down -v
```

### Comandos CLI de Airflow

```bash
# Listar todos los DAGs
docker exec airflow_webserver airflow dags list

# Disparar un DAG manualmente
docker exec airflow_webserver airflow dags trigger etl_pipeline

# Pausar un DAG
docker exec airflow_webserver airflow dags pause etl_pipeline

# Despausar un DAG
docker exec airflow_webserver airflow dags unpause etl_pipeline

# Listar todas las tareas en un DAG
docker exec airflow_webserver airflow tasks list etl_pipeline
```

### Comandos de Gestión de Archivos

```bash
# Ver archivos generados
ls -la storage/extract/
ls -la storage/transform/
ls -la storage/load/

# Ver contenido de un archivo específico
cat storage/extract/data_20240115_143052.csv

# Limpiar archivos antiguos (opcional)
rm storage/extract/*.csv
rm storage/transform/*.csv
rm storage/load/*.csv
```

## Solución de Problemas

### Puerto 8080 Ya en Uso

Cambia el puerto del webserver en `docker-compose.yml`:

```yaml
ports:
  - "8081:8080"
```

### Servicios No se Inician

Revisa los logs en busca de errores:

```bash
docker-compose logs
```

Espera a que la base de datos se inicialice (puede tomar 30-60 segundos).

### El DAG No Aparece

1. Asegúrate de que los archivos del DAG están en el directorio `dags/`
2. Revisa si hay errores de sintaxis de Python en los archivos del DAG
3. Espera unos segundos para que Airflow escanee nuevos DAGs
4. Recarga la interfaz web

### Directorios de Storage No Encontrados

Asegúrate de que los directorios de storage existen:

```bash
mkdir -p storage/extract storage/transform storage/load
```

### Tareas Fallando

1. Revisa los logs de tareas en la interfaz de Airflow
2. Asegúrate de que pandas y numpy están instalados en el contenedor de Airflow
3. Verifica que las rutas de archivos son correctas

## Limpieza

Para eliminar todo completamente:

```bash
# Detener y eliminar contenedores y volúmenes
docker-compose down -v

# Eliminar archivos y directorios generados
rm -rf logs/* storage/extract/* storage/transform/* storage/load/*
```

## Próximos Pasos

- Añadir validación de datos y chequeos de calidad
- Implementar manejo de errores y reintentos
- Conectar a bases de datos reales (PostgreSQL, MySQL)
- Añadir notificaciones por email en caso de fallo
- Implementar procesamiento incremental de datos
- Añadir particionado de datos por fecha
- Crear seguimiento de linaje de datos
- Implementar estrategias de archivo de datos

## Licencia

Este es un ejemplo mínimo con fines educativos. Siéntete libre de usar y modificar según sea necesario.
