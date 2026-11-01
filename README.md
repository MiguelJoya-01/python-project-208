# Gestor de tareas

[![hexlet-check](https://github.com/MiguelJoya-01/python-project-208/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MiguelJoya-01/python-project-208/actions)
[![Coverage](https://github.com/MiguelJoya-01/python-project-208/actions/workflows/coverage.yml/badge.svg)](https://github.com/MiguelJoya-01/python-project-208/actions)

Aplicación web para gestionar tareas, organizada en estados y etiquetas. Permite crear, consultar, editar y eliminar tareas, asignar responsables y filtrar los registros según distintos criterios.

**Aplicación desplegada:** https://hexlet-code-3qlk.onrender.com

## Funcionalidades

- Registro, autenticación y gestión de usuarios.
- Creación, edición y eliminación de estados.
- Creación, edición y eliminación de etiquetas.
- Creación, consulta y edición de tareas.
- Asignación de responsables a las tareas.
- Eliminación de tareas únicamente por sus autores.
- Filtrado de tareas por estado, responsable y etiqueta.
- Opción para mostrar únicamente las tareas propias.
- Protección de registros relacionados para evitar eliminaciones inconsistentes.

## Tecnologías

- Python 3.12
- Django
- SQLite y PostgreSQL
- Bootstrap 5
- django-filter
- Gunicorn
- WhiteNoise
- Sentry SDK
- Bugsink
- uv
- GitHub Actions

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/MiguelJoya-01/python-project-208.git
cd python-project-208
```

Instala las dependencias:

```bash
make install
```

Crea un archivo `.env` en la raíz del proyecto y configura las variables de entorno:

```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,webserver
DATABASE_URL=
SENTRY_DSN=
SENTRY_ENVIRONMENT=development
```

Si utilizas una base de datos PostgreSQL, configura también `DATABASE_URL` con la cadena de conexión correspondiente.

Ejecuta las migraciones:

```bash
uv run python manage.py migrate
```

Inicia el servidor de desarrollo:

```bash
uv run python manage.py runserver
```

Abre http://127.0.0.1:8000/ en tu navegador.

## Pruebas y cobertura

Ejecuta las pruebas automatizadas:

```bash
uv run python manage.py test
```

Para ejecutar las pruebas y generar el informe de cobertura:

```bash
uv run python -m coverage run manage.py test
uv run python -m coverage report
```

El proyecto utiliza Coverage.py con un umbral mínimo de cobertura del **90 %**, configurado en `.coveragerc`.

GitHub Actions ejecuta automáticamente las pruebas y comprueba que se alcance el umbral establecido al realizar cambios en la rama `main` o mediante pull requests.

## Despliegue

La aplicación está desplegada en Render:

https://hexlet-code-3qlk.onrender.com

Configuración de Render:

- **Build Command:** `make build`
- **Start Command:** `make render-start`

La configuración de producción utiliza variables de entorno para gestionar la clave secreta, el modo de depuración, los hosts permitidos y la conexión a la base de datos.

Los errores de la aplicación se supervisan mediante Sentry SDK y Bugsink.

## Autor

Miguel Joya

Proyecto desarrollado como parte del curso de programación de Hexlet.
