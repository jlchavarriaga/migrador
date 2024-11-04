# Migrador de Transacciones
Este proyecto es un servicio Django diseñado para migrar y gestionar datos relacionados con clientes y sus transacciones mediante archivos de Excel. La aplicación ofrece una interfaz web para CRUD de entidades como Instituciones, Clientes, Cuentas y Transacciones, así como una API REST que permite exponer estos recursos como microservicios.

## Estructura del proyecto
    django_app/
    ├── manage.py
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
    │   ├── base.html
    │   ├── login.html
    │   ├── cargar_transacciones.html
    │   ├── transacciones_cuenta.html
    │   ├── 404.html
    │   ├── clientes/
    │   │   ├── cliente_list.html
    │   │   ├── cliente_form.html
    │   │   └── cliente_detail.html
    │   ├── cuentas/
    │   │    ├── cuenta_list.html
    │   │    ├── cuenta_form.html
    │   │    └── cuenta_detail.html
    │   └── institucion/
    │       ├── institucion_confirm_delete.html
    │       ├── institucion_form.html
    │       └── institucion_list.html
    README.md

## Configuración y Preparación

## USO
### 0. Clonar el Repositorio

Primero, descarga o clona el proyecto desde el repositorio. Usa el siguiente comando para clonar el repositorio en tu máquina local:

```bash
git clone https://github.com/jlchavarriaga/migrador.git
```

Luego, navega al directorio del proyecto:
```bash
cd migrador
```

### 1. Construir y Ejecutar los Contenedores
Ejecuta los siguientes comandos para construir los contenedores Docker y ejecutarlos en segundo plano:
```bash
docker-compose build
docker-compose up -d
```

### 2. Aplicar las migraciones iniciales para Django
Aplica las migraciones para configurar la base de datos según los modelos de Django:

```bash
docker-compose run web python manage.py migrate
```

### 3. Creación del SuperUsuario
Crea un superusuario para acceder a la interfaz de administración de Django:


```bash
docker-compose run web python manage.py createsuperuser
```

#### Credenciales de Ejemplo
- Usuario: admin
- Contraseña: admin1234

### 4. Acceso a la aplicación
Una vez que los contenedores están en ejecución y las migraciones se han aplicado correctamente, puedes acceder a la aplicación en tu navegador:


- Interfaz principal: http://localhost:8000
- CRUD de Clientes: http://localhost:8000/clientes/
- CRUD de Cuentas: http://localhost:8000/cuentas/


## CREACIÓN
### 1. Creación del Proyecto Django
```bash
docker-compose run web django-admin startproject myproject .
```

## 2. creación  de la aplicación en Django
```bash
docker-compose run web python manage.py startapp app_banco
```

## 3. Construir y Ejecutar los Contenedores
```bash
docker-compose build
docker-compose up -d
```

## 4. Aplicar las migraciones iniciales para Django
```bash
docker-compose run web python manage.py migrate
```

## 5. Generar los archivos de migración despues de construir los modelos
```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

## 6. Creación del SuperUsuario
```bash
docker-compose run web python manage.py createsuperuser
```

### Credenciales de Ejemplo
- admin
- admin1234

# 7. Acceso a la aplicación
- Interfaz principal: http://localhost:8000
- CRUD de Clientes: http://localhost:8000/clientes/
- CRUD de Cuentas: http://localhost:8000/cuentas/

# Procesos de Carga y Descarga de Transacciones
## Carga de Transacciones desde un Archivo de Excel


### Opción 1: Montar Carpeta de Descargas en el Contenedor (Temporalmente)
```bash
    docker-compose run -v /ruta/a/tu/carpeta/descargas:/app/descargas web python manage.py load_transactions /app/descargas/transacciones_prueba.xlsx
```

### Opción 2: Copiar el Archivo Directamente al Contenedor
Obtén el nombre del contenedor ejecutando:
```bash
    docker ps
```
Usa el siguiente comando para copiar el archivo al contenedor:

```bash
    docker cp /ruta/a/tu/carpeta/descargas/transacciones_prueba.xlsx nombre_del_contenedor:/app/transacciones_prueba.xlsx
```
Ejemplo en Windows:

```bash
        docker cp C:\Users\Usuario\Downloads\transacciones_prueba.xlsx django_app-web-1:/app/transacciones_prueba.xlsx
```

ejecutar el comando load_transactions

```bash
        docker-compose run web python manage.py load_transactions /app/transacciones_prueba.xlsx
        docker exec -it django_app-web-1 python manage.py load_transactions /app/transacciones_prueba.xlsx
 ```
### Opción 3: Ejecución Local (sin Docker)
Desde windows
```bash
    python -m venv venv
    venv\Scripts\activate
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py load_transactions /ruta/al/archivo.xlsx
    deactivate
```

# Ejecutar el Proceso de Descarga de las transacciones
## Ejecución Local
```bash
    python manage.py export_transactions /ruta/donde/guardar/transacciones_exportadas.xlsx
```
## Ejecución en el Contenedor Docker
```bash
    docker-compose run web python manage.py export_transactions /app/transacciones_exportadas.xlsx
    docker exec -it django_app-web-1 python manage.py export_transactions /app/transacciones_prueba.xlsx
```