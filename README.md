# Django App Modular

## Project Structure

```txt
django_modular_project/
├── manage.py
├── django_modular_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── module_engine/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── module_engine/
│   │       ├── module_list.html
│   │       └── module_detail.html
│   ├── urls.py
│   └── views.py
└── product_module/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── templates/
    │   └── product_module/
    │       ├── product_list.html
    │       ├── product_create.html
    │       ├── product_update.html
    │       └── product_detail.html
    ├── urls.py
    └── views.py
```

## Role User

manager_user : Project123
normal_user  : Project123
