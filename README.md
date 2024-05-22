# Taskaroo - Backend

## Tabla de contenido

- [Descripción](#descripción)
- [Sitio web](#sitio-web)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Uso](#uso)
- [Recomendación](#recomendación)
- [Base de datos](#base-de-datos)
  - [Relaciones](#relaciones)
  - [Tabla users](#tabla-users)
  - [Tabla tasks](#tabla-tasks)
- [Estructura de archivos](#estructura-de-archivos)
- [Rutas](#rutas)
- [Autor](#autor)

## Descripción

Este es el backend de la aplicación Taskaroo, una aplicación de gestión de tareas para cada uno de los usuarios creados en la aplicación. En este backend se encuentran las rutas y controladores necesarios para la creación, edición y visualización de tareas para cada uno de los usuarios que permite crear la aplicación.

## Sitio web

La API se puede usar en el siguiente enlace: [Documentación de la API](https://taskaroo-backend-yjo8.onrender.com/docs)

## Tecnologías

- [Python](https://www.python.org/) - Lenguaje de programación utilizado. (3.12)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework utilizado para la creación de la API.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Librería utilizada para la validación de datos.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Librería utilizada para la conexión con la base de datos.
- [MySQL](https://www.mysql.com/) - Base de datos utilizada para el almacenamiento de los datos.

## Instalación

Para instalar el proyecto en tu máquina local, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local.  
```
git clone https://github.com/sacastrot/taskaroo-backend.git
```
2. Crea un entorno virtual en la raíz del proyecto.
`` python -m venv venv``
3. Activa el entorno virtual.
`` venv\Scripts\activate``
4. Instala las dependencias del proyecto.
`` pip install -r requirements.txt``
5. Crea un archivo .env en el modulo (carpeta) sql_app con las siguientes variables de entorno (.env.demo)
```
DATABASE_NAME = "db-name"
DATABASE_USER = "user-name"
DATABASE_PASSWORD = "user-password"
DATABASE_HOST = "host-db"
DATABASE_PORT = "port-db"
```
6. Ejecuta el proyecto.
``  uvicorn sql_app.main:app --reload ``
7. Accede a la documentación de la API en tu navegador.  
```
http://localhost:8000/docs
```

## Uso

Una vez el proyecto esté corriendo, puedes acceder a la documentación de la API en tu navegador y probar los diferentes endpoints que se encuentran disponibles. Adicionalmente puede dirigirse al repositorio del frontend de la aplicación [Taskaroo-frontend](https://github.com/sacastrot/taskaroo-frontend.git) para visualizar la aplicación completa.

## Recomendación

Considere agregar los dominios del frontend en la sección de configuración de CORS en el backend para evitar problemas de CORS en el frontend.

## Base de datos

Para la creación de la base de datos se utilizó PostgreSQL. La base de datos tiene las siguientes tablas:

- users: Tabla que almacena la información de los usuarios de la aplicación.
- tasks: Tabla que almacena la información de las tareas de los usuarios.

### Relaciones

Las relaciones entre las tablas son las siguientes:

- users.id -> tasks.user_id
Un usuario puede tener muchas tareas, pero una tarea solo puede pertenecer a un usuario.

### Tabla users

| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | Identificador único del usuario. |
| email | String | Correo electrónico del usuario. |
| name | String | Nombre del usuario. |
| hashed_password | String | Contraseña del usuario encriptada. |
| is_active | Boolean | Indica si el usuario está activo. |
| tasks | Relationship | Relación con la tabla tasks. |

### Tabla tasks
| Campo | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | Identificador único de la tarea. |
| title | String | Título de la tarea. |
| description | String | Descripción de la tarea. |
| status | String | Estado de la tarea. |
| owner_id | Integer | Identificador del usuario dueño de la tarea. |

## Estructura de archivos

El proyecto se encuentra organizado de la siguiente manera:

- **sql_app**: Módulo principal del proyecto.
  - **__init__**: Archivo de inicialización de la aplicación.
  - **.env.demo**: Archivo de ejemplo para las variables de entorno.
  - **crud**: Contiene las funciones necesarias para la creación, lectura,
    actualización y eliminación de los datos en la base de datos.
  - **database**: Contiene la configuración de la base de datos.
  - **main**: En este archivo se encuentra la configuración de la aplicación y las rutas de la API. Y se ejecuta la aplicación.
  - **models**: Contiene las clases de los modelos de la base de datos.
  - **schemas**: Contiene las clases de los esquemas de los modelos. Que permiten la validación de los datos.

## Rutas
Las rutas disponibles se pueden consultar en la documentación de la API 
en el navegador, FastAPI genera la documentación automáticamente 
en la ruta: [End points](https://taskaroo-backend-yjo8.onrender.com/docs).

En general hay rutas para:
- **Crear usuario**:

| Método | Ruta | Descripción |
| --- | --- | --- |
| POST | /users/ | Permite crear un usuario en la aplicación |


- **Obtener todos los usuario**: 

| Método | Ruta | Descripción |
| --- | --- | --- |
| GET | /users/ | Permite obtener todos los<br/> usuarios de la aplicación |

- **Crear una tarea para un usuario**:

| Método | Ruta | Descripción                                              |
| --- | --- |----------------------------------------------------------|
| POST | /users/{user_id}/tasks/ | Permite crear una tarea<br/> para un usuario en la aplicación |

- **Obtener todas las tareas de un usuario**: GET: /users/{user_id}/tasks/


| Método | Ruta | Descripción |
| --- | --- | --- |
| GET | /users/{user_id}/tasks/ | Permite obtener todas las tareas<br/> de un usuario en la aplicación |


- **Actualizar una tarea de un usuario**: 


| Método | Ruta              | Descripción |
| --- |-------------------| --- |
| PUT | /tasks/{task_id}/ | Permite actualizar una tarea<br/> de un usuario en la aplicación |

## Autor

Santiago Castro - Desarrollador de software y estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia.

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)](https://github.com/sacastrot)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/santiago-castro-tabares/)
[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Profile-blue?style=flat-square&logo=stackoverflow)](https://stackoverflow.com/users/19891867/santiago)