# Proyecto Django - mi_primera_pagina_Oviedo

## Descripción
Proyecto de práctica para aprender MVT en Django. Contiene un modelo `Producto`, una vista que lista productos y un template.

## Cómo ejecutar

1. Crear y activar entorno virtual:
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Crear superusuario (opcional, para usar admin):
   ```bash
   python manage.py createsuperuser
   ```

5. Ejecutar servidor:
   ```bash
   python manage.py runserver
   ```

6. Probar:
   - http://127.0.0.1:8000/ → Lista de productos
   - http://127.0.0.1:8000/admin/ → Panel admin para agregar productos
