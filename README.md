# Taskaroo-backend

## Description

Este es el backend de la aplicación Taskaroo, una aplicación de gestión de tareas para cada uno de los usuarios creados en la aplicación. En este backend se encuentran las rutas y controladores necesarios para la creación, edición y visualización de tareas para cada uno de los usuarios que permite crear la aplicación. 

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

## Autor

Santiago Castro - Desarrollador de software y estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia.

- [LinkedIn](www.linkedin.com/in/santiago-castro-tabares)
- [GitHub](https://github.com/sacastrot)
- [Stack Overflow](https://stackoverflow.com/users/19891867/santiago)
- Email: sacastrot@unal.edu.co

