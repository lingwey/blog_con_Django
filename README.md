# Proyecto de Blog con Django

## Descripción
Este es un proyecto de blog creado con Django. El proyecto incluye funcionalidades como compartir posts, comentarios, búsqueda de posts, y etiquetado de posts utilizando `django-taggit`.

## Características
- **Gestión de Posts**: Crear, leer, actualizar y eliminar posts.
- **Comentarios**: Los usuarios pueden comentar en los posts.
- **Etiquetado**: Los posts pueden ser etiquetados utilizando `django-taggit`.
- **Búsqueda**: Implementación de búsqueda para encontrar posts por título y contenido.
- **Sitemap**: Generación de sitemap utilizando `django.contrib.sitemaps`.
- **Feeds**: Feeds RSS para los posts más recientes.
- **Tags y Filtros Personalizados**: Utiliza tags y filtros personalizados en las plantillas.

## Instalación
Sigue estos pasos para configurar el proyecto en tu entorno local:

1. Clonar el repositorio:
   ```bash
     git clone https://github.com/lingwey/blog_con_Django
   ```
2.Crear un entorno virtual:
  ```bash
     python -m venv env
     source env/bin/activate  # En Windows: env\Scripts\activate
  ```
3.Instalar las dependencias:
```bash
        pip install -r requirements.txt
```
4.Configurar la base de datos:
  Edita el archivo settings.py y configura la base de datos PostgreSQL.
5.Aplicar las migraciones:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
6.Crear un superusuario:
  ```bash
  python manage.py createsuperuser
 ```
7.Ejecutar el servidor de desarrollo:
  ```bash
  python manage.py runserver
 ```


## Dependencias
El proyecto utiliza las siguientes librerías:
- **Django**
- **django-taggit**
- **django.contrib.sitemaps**
- **django.contrib.postgres**
- **psycopg2-binary**

## Configuración de Email
Para habilitar la funcionalidad de compartir posts por email, configura las credenciales de tu servicio de email en settings.py:
``` python
 EMAIL_HOST= 'smtp.gmail.com'
 EMAIL_HOST_USER='tu-email@gmail.com'
 EMAIL_HOST_PASSWORD='tu-contraseña-de-app'
 EMAIL_PORT=587
 EMAIL_USE_TLS= True
```
## Estructura del Proyecto
- **app_blog**: Contiene la lógica principal de la aplicación.
- **models.py**: Define los modelos de la base de datos.
- **views.py**: Contiene las vistas de la aplicación.
- **forms.py**: Define los formularios utilizados en la aplicación.
- **urls.py**: Define las rutas de la aplicación.
- **sitemaps.py**: Configura los sitemaps.
- **feeds.py**: Configura los feeds RSS.
- **admin.py**: Configura la administración de los modelos.
- **templatetags/blog_tags.py**: Define tags y filtros personalizados.
- **templates/**: Contiene las plantillas HTML.

**blog**: Configuración del proyecto Django.
- **settings.py**: Configuraciones del proyecto.
- **urls.py**: Rutas principales del proyecto.

