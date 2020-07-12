# Flask Scaffold

This is a scaffold of a project, it's designed based on Flask and blueprint
has been integrated into the packages below:

- flask-sqlalchemy
- flask-wtf
- flask-bootstrap
- flask-migrate
- flask-script

# Project Structure Prototype

Use Flask blueprint to subdivide the project into separate modules.
Modules are distinguished from each other by feature or segments

The project structure prototype in below:

```
.
├── app
│   ├── module_1
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── module_1.j2
│   │   └── views.py
│   ├── module_2
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── module_2.j2
│   │   └── views.py
│   └── templates
│       └── base.j2
├── config.py
├── manage.py
├── pyproject.toml
├── README.md
└── tests
    ├── __init__.py
    └── test_basic.py
```

# Scaffold Project Structure
```
.
├── app
│   ├── auth
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── auth.j2
│   │   └── views.py
│   ├── core
│   │   ├── form.py
│   │   ├── __init__.py
│   │   ├── templates
│   │   │   └── index.j2
│   │   └── views.py
│   ├── errors
│   │   ├── handlers.py
│   │   ├── __init__.py
│   │   └── templates
│   │       ├── 404.j2
│   │       └── 500.j2
│   ├── __init__.py
│   └── templates
│       └── base.j2
├── config.py
├── manage.py
├── pyproject.toml
├── README.md
└── tests
    ├── __init__.py
    ├── test_basic.py
    └── test_user_model.py

```

# Quick Start
1. Clone this repo
    ```
    $ git clone <this repo>
    $ cd flask-prototype
    ```
2. Initialize and activate a virtualenv:
    ```
    $ poetry shell
    ```
3. Install the dependencies:
   ```
   $ poetry update
   ```
4. Run the development server:
   ```
   $ python manage.py runserver
   ```
5. Navigate to http://localhost:5000/

# Manage CLI

This prototype has support manage cli.

The list command below:

- Change project name:
    > python manage.py projectname `project_name`

- Run server:
    > python manage.py runserver

- Run tests:
    > python manage.py test

- Make migration:
    > python manage.py migrations

- Migrate database:
    > python manage.py migrate
