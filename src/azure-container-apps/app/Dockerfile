FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for certificates
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

# Fix for "SSL record layer failure": Allow TLS 1.2 by lowering the security level of OpenSSL
RUN sed -i 's/CipherString = DEFAULT@SECLEVEL=2/CipherString = DEFAULT@SECLEVEL=1/g' /etc/ssl/openssl.cnf

# Copy the certificate (must be run from project root: docker build -t aca-api -f app/Dockerfile .)
COPY ./certificates/emulator.crt /usr/local/share/ca-certificates/emulator.crt
RUN update-ca-certificates

# Copy requirements and install
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY ./app/ .

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
