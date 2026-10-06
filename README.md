# ProyectoDjango

Portfolio personal y blog construidos con Django.

## Estructura

- `config/`: configuración, rutas y entrada WSGI del proyecto.
- `portfolio/`: vista, URL y plantilla `index.html` del portfolio.
- `blog/`: modelos, formularios, vistas, administración, plantillas y estilos del blog.
- `templates/base.html`: layout compartido por el portfolio y el blog.
- `static/css/styles.css`: estilos generales y del portfolio.
- `static/assets/`: imágenes, multimedia y CV.
- `blog/static/blog/styles.css`: estilos específicos del blog.

## Puesta en marcha

En Windows, desde la carpeta del proyecto:

```powershell
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Abrir `http://127.0.0.1:8000/` para el portfolio, `/blog/` para las entradas y `/admin/` para administrar posts y eliminar comentarios.

Las entradas se ordenan automáticamente de la más nueva a la más antigua. Cada post puede tener texto, una imagen o archivo cargado desde el panel y una imagen multimedia de respaldo mediante `media_url`.