# 🏦 API Bancaria con FastAPI, MongoDB y Docker

![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-brightgreen?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4.x-green?logo=mongodb&logoColor=white)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen?logo=pytest)

Una API RESTful desarrollada en Python que permite:

- ✅ Crear cuentas bancarias
- ✅ Actualizar el saldo de una cuenta
- ✅ Listar todas las cuentas existentes

---

## 🚀 Tecnologías Utilizadas

| Herramienta     | Uso principal                      |
|----------------|------------------------------------|
| **FastAPI**    | Framework para la API              |
| **MongoDB**    | Base de datos NoSQL                |
| **Motor**      | Cliente async para MongoDB         |
| **Uvicorn**    | Servidor ASGI                      |
| **Pydantic**   | Validación de datos con tipado     |
| **Docker**     | Empaquetado y despliegue           |
| **Pytest**     | Pruebas unitarias y de integración |

---

## 🧬 Estructura del Proyecto

```bash
bank-project/
├── app/
│   ├── api/             # Rutas de la API
│   ├── core/            # Configuración de base de datos
│   ├── models/          # Modelos de entrada
│   ├── repositories/    # Lógica de acceso a datos (MongoDB)
│   ├── schemas/         # Esquemas de salida (DTOs)
│   └── services/        # Lógica de negocio
├── tests/               # Pruebas unitarias y de endpoints
├── .env.example         # Variables de entorno necesarias
├── Dockerfile           # Imagen para la API
├── docker-compose.yml   # Orquestación FastAPI + MongoDB
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación
```

---

## 🚧 Despliegue con Docker

### 1. Clona el repositorio
```bash
git clone https://github.com/Charbrown08/bank-api.git
cd bank-api
```

### 2. Crea el archivo `.env`

Usa el archivo de ejemplo:
```bash
cp .env.example .env
```

### 3. Levanta los servicios con Docker Compose
```bash
docker-compose up --build
```

### 4. Accede a la API

<!-- - API: http://localhost:8000 -->
- Documentación interactiva: http://localhost:8000/docs

---

## ✅ Ejecutar Pruebas Unitarias

### 1. Accede al contenedor de la API:
```bash
docker exec -it bank_api bash
```

### 2. Ejecuta las pruebas con `pytest`:
```bash
pytest
```

> Las pruebas mockean el acceso a la base de datos para garantizar independencia.

---

## 🔐 Variables de Entorno

El archivo `.env.example` incluye:

```env
MONGO_URI=mongodb://mongo:27017
```

---

## 🌍 Endpoints Disponibles

### 🚀 Crear una Cuenta
```
POST /api/v1/accounts
```
**Body:**
```json
{
  "owner_name": "Carlos Moreno"
}
```
**Respuesta:**
```json
{
  "id": "uuid-generado"
}
```

### 💸 Actualizar Saldo
```
PATCH /api/v1/accounts/{account_id}
```
**Body:**
```json
{
  "amount": 150.0
}
```
**Respuesta:**
```json
{
  "balance": 300.0
}
```

### 📄 Listar Cuentas
```
GET /api/v1/accounts
```
**Respuesta:**
```json
[
  {
    "id": "...",
    "owner_name": "Carlos",
    "balance": 100.0
  }
]
```

---

## 💡 Arquitectura y Patrones

Este proyecto utiliza una **arquitectura modular basada en Clean Architecture simplificada**, buscando una separación clara de responsabilidades y fácil escalabilidad:

### 🧱 Decisiones de Diseño:

- **FastAPI** como core de API RESTful moderno, asíncrono y tipado.
- **MongoDB** como base de datos NoSQL, ideal para prototipos ágiles y estructuras flexibles.
- **Motor** por ser cliente asíncrono compatible con `async/await`, mejorando el rendimiento.
- **Docker** para portabilidad y despliegue consistente.

### 📦 Componentes y Patrones:

- **Repository Pattern** (`app/repositories/`): abstrae el acceso a MongoDB, permite mockeo en pruebas y mantiene la lógica de datos separada.
- **Service Layer** (`app/services/`): encapsula reglas de negocio, centraliza validaciones y coordina múltiples acciones (ej. verificar saldo antes de actualizar).
- **DTOs con Pydantic** (`app/models/` y `app/schemas/`): definen estructuras claras de entrada/salida, validan los datos automáticamente y mejoran la documentación.
- **Routing limpio** (`app/api/`): define endpoints de forma declarativa, legible y mantenible.

> Esta estructura permite escalar el sistema fácilmente agregando nuevas entidades, sin comprometer la calidad ni el orden del código.

---

## ✍️ Autor

Desarrollado con ❤️ por **Carlos Andrés Moreno Jiménez**

---

## 🪪 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

