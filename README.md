# Gestor de tareas

[![hexlet-check](https://github.com/MiguelJoya-01/python-project-208/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MiguelJoya-01/python-project-208/actions)

Aplicación web desarrollada con Django como proyecto de aprendizaje de Códica.

## Aplicación desplegada

**URL:** https://hexlet-code-3qlk.onrender.com

## Descripción

Aprenderás con un proyecto real cómo diseñar bases de datos, usar plataformas PaaS, integrar un servicio de seguimiento de errores, trabajar con ORM, Django, plantillas y Bootstrap.

Proyecto de aprendizaje de Códica: https://app.codica.la/programs/python

Así debería funcionar: https://files.hexlet.app/a/64zdfp

## Stack

- Python
- Django
- Gunicorn
- SQLite
- PostgreSQL (configurable mediante variables de entorno)
- WhiteNoise
- uv

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/MiguelJoya-01/python-project-208.git
cd python-project-208
```

Instala las dependencias:

```bash
uv sync
```

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,webserver
```

Ejecuta las migraciones:

```bash
uv run python manage.py migrate
```

Inicia el servidor de desarrollo:

```bash
uv run python manage.py runserver
```

Abre http://127.0.0.1:8000/ en tu navegador.

## Despliegue

El proyecto está desplegado en Render.

- **Build Command:** `make build`
- **Start Command:** `make render-start`

La configuración de producción utiliza variables de entorno para gestionar la clave secreta, el modo de depuración y la conexión
