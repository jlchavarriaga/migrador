# migrador
Servicio para migrar un archivo de excel con datos relacionados a clientes y sus transacciones

# Estructura del proyecto
    django_app/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── app/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    ├── management/
    │   ├── commands/
    │   │   └── export_transactions.py
    │   │   └── load_transactions.py
    ├── templates/
    │   ├── clientes/
    │   │   ├── cliente_list.html
    │   │   ├── cliente_form.html
    │   │   └── cliente_detail.html
    │   └── cuentas/
    │       ├── cuenta_list.html
    │       ├── cuenta_form.html
    │       └── cuenta_detail.html

# creación  del proyecto Django
docker-compose run web django-admin startproject myproject .

# creación  de la aplicación en Django
docker-compose run web python manage.py startapp app_banco

# Construir y Ejecutar los Contenedores
docker-compose build
docker-compose up -d

# Aplicar las migraciones iniciales para Django
docker-compose run web python manage.py migrate

# Generar los archivos de migración despues de construir los modelos
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

# SuperUsuario
docker-compose run web python manage.py createsuperuser

admin
admin1234

# acceder a la aplicación
 http://localhost:8000.
 http://127.0.0.1:8000/clientes/
 http://127.0.0.1:8000/cuentas/

# Ejecutar el Proceso de Carga de las transacciones
Montar la Carpeta de Descargas en el Contenedor (Temporalmente)
    docker-compose run -v /ruta/a/tu/carpeta/descargas:/app/descargas web python manage.py load_transactions /app/descargas/transacciones_prueba.xlsx

Copiar el Archivo Directamente al Contenedor
    docker ps
    usa   docker cp /ruta/a/tu/carpeta/descargas/transacciones_prueba.xlsx nombre_del_contenedor:/app/transacciones_prueba.xlsx
        por ejemplo:    docker cp C:\Users\Usuario\Downloads\transacciones_prueba.xlsx django_app-web-1:/app/transacciones_prueba.xlsx
    ejecutar
        docker-compose run web python manage.py load_transactions /app/transacciones_prueba.xlsx
        docker exec -it django_app-web-1 python manage.py load_transactions /app/transacciones_prueba.xlsx


Desde windows
    python -m venv venv
    venv\Scripts\activate
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py load_transactions /ruta/al/archivo.xlsx
    deactivate

# Ejecutar el Proceso de Descarga de las transacciones
    python manage.py export_transactions /ruta/donde/guardar/transacciones_exportadas.xlsx
    docker-compose run web python manage.py export_transactions /app/transacciones_exportadas.xlsx
    docker exec -it django_app-web-1 python manage.py export_transactions /app/transacciones_prueba.xlsx
