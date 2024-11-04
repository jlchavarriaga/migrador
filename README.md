# migrador
Servicio para migrar un archivo de excel con datos relacionados a clientes y sus transacciones

# creación  del proyecto Django
docker-compose run web django-admin startproject myproject .

# Construir y Ejecutar los Contenedores
docker-compose build
docker-compose up -d

# Aplicar las migraciones iniciales para Django
docker-compose run web python manage.py migrate


# SuperUsuario
docker-compose run web python manage.py createsuperuser

admin
admin1234

# acceder a la aplicación
 http://localhost:8000.