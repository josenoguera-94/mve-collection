# Ejemplos Mínimos Viables (MVE)

Una colección curada de ejemplos de código mínimos y listos para producción, diseñados para ayudar a los desarrolladores a comprender e implementar rápidamente patrones y tecnologías comunes.

## 🎯 Objetivo

Este repositorio proporciona **ejemplos limpios, mínimos y completamente funcionales** que demuestran tecnologías, patrones o integraciones específicas. Cada ejemplo es:

- **Autocontenido**: Todo lo que necesitas está incluido
- **Bien documentado**: Explicaciones claras e instrucciones paso a paso
- **Listo para contenedores**: Configuración de Dev Container para un entorno de desarrollo consistente
- **Gestión de dependencias**: Usando `uv` para una gestión rápida y confiable de dependencias de Python

## 📁 Estructura del Repositorio

```
mve-collection/
├── README.md                          # Este archivo
└── src/
    ├── postgres-docker-sqlalchemy/    # Ejemplo 1
    │   ├── .devcontainer.json
    │   ├── pyproject.toml
    │   ├── uv.lock
    │   ├── README.md
    │   └── [archivos del ejemplo]
    ├── mongo-docker-mongoengine/      # Ejemplo 2
    │   ├── .devcontainer.json
    │   ├── pyproject.toml
    │   ├── uv.lock
    │   ├── README.md
    │   └── [archivos del ejemplo]
    └── [más ejemplos]/
```

### Estructura de Cada MVE

Cada ejemplo sigue una estructura consistente:

```
src/[nombre-mve]/
├── .devcontainer.json     # Configuración de Dev Container
├── pyproject.toml         # Dependencias del proyecto (uv)
├── uv.lock               # Dependencias bloqueadas
├── README.md             # Documentación específica del ejemplo
└── [archivos fuente]     # Archivos de código y configuración
```

## 🚀 Inicio Rápido

### Requisitos Previos

- [Docker](https://www.docker.com/get-started) instalado
- [VS Code](https://code.visualstudio.com/) con la extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Ejecutar un Ejemplo

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/raulcastillabravo/mve-collection.git
   cd mve-collection
   ```

2. **Abrir un ejemplo en VS Code**:
   ```bash
   cd src/postgres-docker-sqlalchemy
   code .
   ```

3. **Reabrir en Dev Container**:
   - Presiona `F1` o `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
   - Selecciona: **Dev Containers: Reopen in Container**
   - Espera a que el contenedor se construya y las dependencias se instalen

4. **Seguir el README del ejemplo**:
   - Cada ejemplo tiene su propio `README.md` con instrucciones específicas

## 📚 Ejemplos Disponibles

| Ejemplo | Descripción | Tecnologías |
|---------|-------------|--------------|
| [postgres-docker-sqlalchemy](./src/postgres-docker-sqlalchemy/) | Configuración de PostgreSQL con Docker Compose y ORM SQLAlchemy | PostgreSQL, Docker, SQLAlchemy, Python |
| *Más ejemplos próximamente...* | | |

## 🛠️ Stack Tecnológico

### Tecnologías Core
- **Python 3.12+**: Lenguaje de programación principal
- **uv**: Instalador y resolvedor rápido de paquetes de Python
- **Docker**: Contenedorización y orquestación de servicios
- **Dev Containers**: Entornos de desarrollo consistentes

### Tecnologías Específicas por Ejemplo
Cada ejemplo puede incluir tecnologías adicionales como:
- Bases de datos (PostgreSQL, MongoDB, Redis)
- Frameworks web (FastAPI, Flask, Django)
- Colas de mensajes (RabbitMQ, Kafka)
- Y más...

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si tienes un ejemplo mínimo viable que te gustaría compartir:

1. Haz un fork del repositorio
2. Crea un nuevo directorio bajo `src/` con el nombre de tu ejemplo
3. Sigue la estructura estándar (ver arriba)
4. Incluye un `README.md` completo
5. Prueba tu ejemplo en el Dev Container
6. Envía un pull request

### Directrices para Nuevos Ejemplos

- **Mantenlo mínimo**: Solo incluye lo necesario para demostrar el concepto
- **Documenta exhaustivamente**: Explicaciones claras y comandos
- **Usa uv**: Gestiona las dependencias con `pyproject.toml` y `uv.lock`
- **Incluye Dev Container**: Proporciona `.devcontainer.json` para configuración fácil
- **Sigue las mejores prácticas**: Manejo adecuado de errores, variables de entorno, etc.

## 📖 ¿Por Qué Este Repositorio?

Aprender nuevas tecnologías a menudo implica:
- ❌ Navegar por documentación extensa
- ❌ Depurar problemas complejos de configuración
- ❌ Encontrar ejemplos desactualizados
- ❌ Dependencias o configuraciones faltantes

Este repositorio resuelve estos problemas proporcionando:
- ✅ Ejemplos listos para ejecutar
- ✅ Entornos contenedorizados
- ✅ Especificaciones completas de dependencias
- ✅ Documentación clara paso a paso
- ✅ Mejores prácticas y patrones

## 📝 Licencia

Este repositorio es de código abierto y está disponible bajo la [Licencia MIT](LICENSE).

## 🙏 Agradecimientos

Cada ejemplo acredita las tecnologías y recursos que lo hicieron posible. Consulta los READMEs individuales de cada ejemplo para atribuciones específicas.

---

**¡Feliz programación! 🚀**

Si encuentras estos ejemplos útiles, por favor considera darle una ⭐ a este repositorio

## 🌐 Sígueme

Conéctate conmigo en LinkedIn para más contenido y actualizaciones:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raulcastillabravo/)