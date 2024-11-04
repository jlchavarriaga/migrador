# migrador
Servicio para migrar un archivo de excel con datos relacionados a clientes y sus transacciones

# Estructura del proyecto
    django_app/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── app/

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