provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  endpoints {
    secretsmanager = "http://localhost:4566"
  }
}

provider "postgresql" {
  host     = "localhost"
  port     = 5432
  database = "mydb"
  username = "myuser"
  password = "mypassword"
  sslmode  = "disable"
}

# Create Postgres Table
resource "postgresql_table" "users" {
  name     = "users"
  database = "mydb"
  schema   = "public"
  column {
    name = "id"
    type = "integer"
    nullable = false
  }
  column {
    name = "name"
    type = "character varying(100)"
  }
  column {
    name = "email"
    type = "character varying(100)"
  }
  column {
    name = "created_at"
    type = "timestamp without time zone"
  }
}

# Add Primary Key (Terraform postgresql provider trick)
resource "postgresql_extension" "uuid" {
  name = "uuid-ossp"
}

# Secret for the DB URI
resource "aws_secretsmanager_secret" "db_secret" {
  name = "postgres-connection-uri"
}

resource "aws_secretsmanager_secret_version" "db_secret_val" {
  secret_id     = aws_secretsmanager_secret.db_secret.id
  secret_string = "postgresql://myuser:mypassword@host.docker.internal:5432/mydb"
}
