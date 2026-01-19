# Azure Container Apps + Dapr + Cosmos DB

Ejemplo mínimo viable para trabajar con Azure Container Apps localmente usando Dapr y el Emulador de Cosmos DB. Este ejemplo demuestra cómo crear un microservicio que registra usuarios en Cosmos DB sin necesidad de suscripción a Azure.

## Estructura del Proyecto

```
azure-container-apps/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── components/
│   └── statestore.yaml
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── .env
├── main.py
├── pyproject.toml
└── README.md
```

## Prerrequisitos

- Docker y Docker Compose instalados
- VS Code con la extensión Dev Containers (opcional)

## Opción 1: Usando Dev Container (Recomendado)

### Paso 1: Abrir el Proyecto en Dev Container

1. Abre VS Code en la carpeta del proyecto.
2. Presiona `F1` y selecciona: **Dev Containers: Reopen in Container**.
3. Espera a que se construyan los servicios (esto levantará automáticamente el emulador y la app).

### Paso 2: Ejecutar el Ejemplo

Una vez dentro del contenedor, abre una terminal y ejecuta:

```bash
python main.py
```

Deberías ver una salida indicando que el usuario se ha guardado correctamente.

---

## Opción 2: Setup Local (Sin Dev Container)

### Paso 1: Instalar Dependencias

```bash
pip3 install uv && uv sync
```

### Paso 2: Levantar la Infraestructura

```bash
docker-compose up -d
```

### Paso 3: Ejecutar el Ejemplo

```bash
python main.py
```

---

## Componentes del Proyecto

### API Flask (`app/main.py`)

Microservicio que recibe los datos del usuario. La magia aquí es que **no usa el SDK de Cosmos DB**. Se comunica con el sidecar de Dapr mediante HTTP, lo que lo hace totalmente portable.

### Configuración Dapr (`components/statestore.yaml`)

Define el componente de estado. Aquí es donde le decimos a Dapr que use el emulador de Cosmos DB. En producción, solo cambiaríamos este YAML para apuntar a la instancia real.

### Script de Prueba (`main.py`)

Simula una petición externa enviando un JSON con datos de un perfil de LinkedIn.

---

## Variables de Entorno

El archivo `.env` contiene:

```
COSMOS_KEY=C2y6yDjf5/...
COSMOS_URL=https://localhost:8081
```

**Nota**: La clave del emulador es una clave estándar y pública proporcionada por Microsoft para pruebas locales.

---

## Comandos Útiles

### Docker Commands

```bash
# Ver logs de la aplicación
docker logs aca_app

# Ver logs del sidecar de Dapr
docker logs azure-container-apps-app-dapr-1

# Parar todo
docker-compose down
```

---

## Troubleshooting

### Error de Certificado SSL

El emulador de Cosmos DB usa certificados auto-firmados. Dapr ya está configurado para ignorar la validación en este entorno de desarrollo, pero si usas el SDK directamente, podrías necesitar importar el certificado.

### El Explorador de Datos no carga

Asegúrate de que el puerto `1234` está libre. Puedes acceder al explorador mediante `http://localhost:1234` una vez que el contenedor `cosmos_local` esté corriendo.

---

## Clean Up

Para limpiar completamente el entorno:

```bash
docker-compose down -v
docker rmi azure-container-apps-app
```

---

## Siguientes Pasos

- Implementar Pub/Sub con Dapr y Redis.
- Añadir secretos gestionados por Dapr.
- Configurar escalado automático con KEDA.

## Licencia

Este es un ejemplo minimalista con fines educativos. Siéntete libre de usarlo y modificarlo.
