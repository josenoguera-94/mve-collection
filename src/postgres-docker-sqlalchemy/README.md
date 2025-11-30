# PostgreSQL + SQLAlchemy + Docker Example

Minimal viable example to work with PostgreSQL using Docker Compose, SQLAlchemy ORM, and DBeaver.

## Project Structure

```
project/
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── .env
├── models.py
├── pyproject.toml
├── main.py
├── uv.lock
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- VS Code with Dev Containers extension (optional, for dev container setup)
- DBeaver or any PostgreSQL client

## Option 1: Using Dev Container (Recommended)

### Step 1: Open Project in Dev Container

1. Open VS Code in the project folder
2. Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
3. Type and select: **Dev Containers: Reopen in Container**
4. Wait for the container to build and dependencies to install

### Step 2: Start PostgreSQL Container

Inside the dev container terminal:

```bash
docker compose up -d
```

Verify it's running:

```bash
docker ps
```

### Step 3: Create Tables and Insert Data

Run the Python script:

```bash
python main.py
```

You should see output like:

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

## Option 2: Local Setup (Without Dev Container)

### Step 1: Install Python Dependencies

```bash
pip3 install uv && uv sync
```

### Step 2: Start PostgreSQL Container

```bash
docker compose up -d
```

### Step 3: Create Tables and Insert Data

```bash
python main.py
```

## Connecting with DBeaver

### Step 1: Create New Connection

1. Open DBeaver
2. Click on **New Database Connection** (plug icon with +)
3. Select **PostgreSQL**
4. Click **Next**

### Step 2: Configure Connection

Enter the following details:

- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `testdb`
- **Username:** `admin`
- **Password:** `admin123`

### Step 3: Test and Save

1. Click **Test Connection** to verify
2. If successful, click **Finish**

### Step 4: View Data

1. In the Database Navigator, expand your connection
2. Navigate to: `testdb` → `Schemas` → `public` → `Tables` → `users`
3. Right-click on `users` table → **View Data**
4. You should see the 3 users inserted by the Python script

## Database Schema

The `users` table has the following structure:

| Column     | Type                        | Description                |
|------------|-----------------------------|----------------------------|
| id         | INTEGER (Primary Key)       | Auto-incrementing user ID  |
| name       | VARCHAR(100)                | User's full name           |
| email      | VARCHAR(100) (Unique)       | User's email address       |
| created_at | TIMESTAMP                   | Record creation timestamp  |

## Environment Variables

The `.env` file contains:

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=testdb
POSTGRES_PORT=5432
POSTGRES_HOST=localhost
```

You can modify these values as needed. Remember to recreate the containers if you change database credentials.

## Useful Commands

### Docker Commands

```bash
# Start containers
docker compose up -d

# Stop containers
docker compose down

# Stop and remove volumes (delete all data)
docker compose down -v

# View logs
docker compose logs -f

# View only PostgreSQL logs
docker compose logs -f postgres
```

## Troubleshooting

### Port Already in Use

If port 5432 is already in use, change `POSTGRES_PORT` in `.env` to another port (e.g., 5433) and restart:

```bash
docker compose down
docker compose up -d
```

### Connection Refused

Make sure the PostgreSQL container is running:

```bash
docker ps
```

Check the logs for errors:

```bash
docker compose logs postgres
```

### Module Not Found

If you get import errors, install dependencies:

```bash
pip3 install uv && uv sync
```

### Permission Denied (Dev Container)

If you get permission errors with Docker in the dev container, make sure the `docker-outside-of-docker` feature is properly configured in `devcontainer.json`.

## Clean Up

To completely remove everything:

```bash
# Stop and remove containers and volumes
docker compose down -v

# Remove the PostgreSQL image (optional)
docker rmi postgres:15-alpine
```

## Next Steps

- Add more models to `models.py`
- Implement relationships between tables (Foreign Keys)
- Add data validation
- Create API endpoints with FastAPI or Flask
- Add database migrations with Alembic

## License

This is a minimal example for educational purposes. Feel free to use and modify as needed.