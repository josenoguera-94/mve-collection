# PostgreSQL + SQLAlchemy + Docker: Ejemplo Mínimo Viable

Ejemplo mínimo viable (MVE) para trabajar con **PostgreSQL** usando **Docker Compose**, el ORM **SQLAlchemy** y el cliente **DBeaver**.

## Estructura del Proyecto

```
project/
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── .env
├── models.py
├── pyproject.toml
├── main.py
├── uv.lock
└── README.md
```

## Requisitos Previos

  * **Docker** y **Docker Compose** instalados.
  * **VS Code** con la extensión [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) (opcional, para la configuración del contenedor de desarrollo).
  * **DBeaver** o cualquier cliente PostgreSQL.

-----

## Opción 1: Usando Contenedor de Desarrollo (Recomendado)

### Paso 1: Abrir el Proyecto en el Contenedor de Desarrollo

1.  Abre VS Code en la carpeta del proyecto.
2.  Pulsa `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac).
3.  Escribe y selecciona: **Dev Containers: Reopen in Container** (Contenedores de Desarrollo: Reabrir en Contenedor).
4.  Espera a que el contenedor se construya y se instalen las dependencias.

### Paso 2: Iniciar el Contenedor de PostgreSQL

Dentro de la terminal del contenedor de desarrollo:

```bash
docker-compose up -d
```

Verifica que esté corriendo:

```bash
docker ps
```

### Paso 3: Crear Tablas e Insertar Datos

Ejecuta el script de Python:

```bash
python main.py
```

Deberías ver una salida similar a esta:

```
Creating tables...
✓ Tables created successfully

Inserting sample data...
✓ Inserted 3 users successfully

Inserted users:
  - <User(id=1, name='John Doe', email='john@example.com')>
  - <User(id=2, name='Jane Smith', email='jane@example.com')>
  - <User(id=3, name='Bob Johnson', email='bob@example.com')>

✓ Done! You can now connect with DBeaver to see the data.
```

-----

## Opción 2: Configuración Local (Sin Dev Container)

### Paso 1: Instalar Dependencias de Python

```bash
pip3 install uv && uv sync
```

### Paso 2: Iniciar el Contenedor de PostgreSQL

```bash
docker-compose up -d
```

### Paso 3: Crear Tablas e Insertar Datos

```bash
python main.py
```

-----

## 🔗 Conexión con DBeaver

### Paso 1: Crear Nueva Conexión

1.  Abre DBeaver.
2.  Haz clic en **New Database Connection** (icono del enchufe con un +).
3.  Selecciona **PostgreSQL**.
4.  Haz clic en **Siguiente**.

### Paso 2: Configurar la Conexión

Introduce los siguientes detalles:

  * **Host:** `localhost`
  * **Port:** `5432`
  * **Database:** `testdb`
  * **Username:** `admin`
  * **Password:** `admin123`

### Paso 3: Probar y Guardar

1.  Haz clic en **Test Connection** para verificar.
2.  Si es exitoso, haz clic en **Finish**.

### Paso 4: Ver los Datos

1.  En el **Database Navigator**, expande tu conexión.
2.  Navega a: `testdb` → `Schemas` → `public` → `Tables` → **`users`**.
3.  Haz clic derecho sobre la tabla **`users`** → **View Data** (Ver Datos).
4.  Deberías ver los 3 usuarios insertados por el script de Python.

-----

## Esquema de la Base de Datos

La tabla **`users`** tiene la siguiente estructura:

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | `INTEGER` (Clave Primaria) | ID de usuario autoincremental. |
| `name` | `VARCHAR(100)` | Nombre completo del usuario. |
| `email` | `VARCHAR(100)` (Único) | Dirección de correo electrónico del usuario. |
| `created_at` | `TIMESTAMP` | Marca de tiempo de la creación del registro. |

-----

## Variables de Entorno

El archivo **`.env`** contiene lo siguiente:

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=testdb
POSTGRES_PORT=5432
POSTGRES_HOST=localhost
```

Puedes modificar estos valores según sea necesario. Recuerda **recrear los contenedores** si cambias las credenciales de la base de datos.

-----

## Comandos Útiles

### Comandos de Docker

```bash
# Iniciar contenedores
docker-compose up -d

# Detener contenedores
docker-compose down

# Detener y eliminar volúmenes (elimina todos los datos)
docker-compose down -v

# Ver logs
docker-compose logs -f

# Ver solo los logs de PostgreSQL
docker-compose logs -f postgres
```

-----

## Solución de Problemas (Troubleshooting)

### Puerto ya en uso

Si el puerto 5432 ya está en uso, cambia `POSTGRES_PORT` en el archivo `.env` a otro puerto (ej., 5433) y reinicia:

```bash
docker-compose down
docker-compose up -d
```

### Conexión Rechazada

Asegúrate de que el contenedor de PostgreSQL esté corriendo:

```bash
docker ps
```

Comprueba los logs en busca de errores:

```bash
docker-compose logs postgres
```

### Módulo No Encontrado

Si obtienes errores de importación, instala las dependencias:

```bash
pip3 install uv && uv sync
```

### Permiso Denegado (Dev Container)

Si obtienes errores de permisos con Docker dentro del contenedor de desarrollo, asegúrate de que la *feature* `docker-outside-of-docker` esté configurada correctamente en tu `devcontainer.json`.

-----

## Limpieza

Para eliminar completamente todos los contenedores y datos asociados:

```bash
# Detener y eliminar contenedores y volúmenes
docker-compose down -v

# Eliminar la imagen de PostgreSQL (opcional)
docker rmi postgres:15-alpine
```

-----

## Siguientes Pasos

  * Añadir más modelos al archivo `models.py`.
  * Implementar relaciones entre tablas (Claves Foráneas).
  * Añadir validación de datos.
  * Crear *endpoints* de API con **FastAPI** o **Flask**.
  * Añadir migraciones de bases de datos con **Alembic**.

## Licencia

Este es un ejemplo mínimo con fines educativos. Siéntete libre de usarlo y modificarlo según sea necesario.