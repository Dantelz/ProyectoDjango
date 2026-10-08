ProyectoDjango

Secciones Principales del sitio

Portfolio: muestra informacion personal, habilidades y proyectos.
Blog: muestra las publicaciones ordenadas desde la mas nueva hasta la mas antigua. Al abrir una publicacion se puede leer su contenido y dejar un comentario.
Administracion: es el panel que Django ofrece para gestionar los datos. Se ingresa con una cuenta creada para el proyecto.

En el blog tambien hay una opcion Publicar. Al seleccionarla, se solicitan las credenciales admin / admin y luego se muestra un formulario para crear una publicacion con titulo, identificador para la URL, resumen, contenido e imagen. En cada publicacion existe la opcion Eliminar post, que solicita esas mismas credenciales y, si son correctas, elimina la publicacion y sus comentarios.

El usuario admin / admin estan escritas directamente en el codigo. Se incluyeron para practicar el flujo de publicacion y eliminacion, pero no son seguras.

Como ejecutar el proyecto

Se necesita Python. Django esta declarado como dependencia en requirements.txt. En Windows, abri una terminal en la carpeta del proyecto y ejecuta:

    py -m pip install -r requirements.txt
    py manage.py migrate
    py manage.py createsuperuser
    py manage.py runserver

El primer comando instala las dependencias. migrate prepara la base de datos SQLite y aplica los cambios registrados en las migraciones. createsuperuser permite crear una cuenta para ingresar al panel de administracion. Por ultimo, runserver inicia el sitio para probarlo localmente.

Cuando el servidor este iniciado, mediante "python manage.py runserver", se puede acceder a:

- http://127.0.0.1:8000/ para el portfolio.
- http://127.0.0.1:8000/blog/ para el blog.
- http://127.0.0.1:8000/admin/ para el panel de administracion.

Organizacion de los archivos

- manage.py: permite ejecutar comandos de Django, como iniciar el servidor y aplicar migraciones.

- config/: contiene la configuracion general del proyecto y las rutas principales.

- portfolio/: contiene la vista, las rutas y la plantilla principal del portfolio.

- blog/models.py: define que informacion se guarda para cada publicacion y comentario.

- blog/forms.py: define los formularios de publicacion y comentarios.

- blog/views.py: procesa las paginas de listado, detalle, publicacion y eliminacion.

- blog/urls.py: conecta las direcciones del blog con sus vistas.

- blog/admin.py: configura como aparecen las publicaciones y los comentarios en el panel de Django.

- blog/templates/blog/: contiene las plantillas del blog. base.html define la barra de navegacion y el pie; las otras plantillas 
muestran el listado, el detalle y el formulario para publicar.
- templates/base.html: contiene la estructura comun de las paginas y el selector de tema claro u oscuro.

- static/css/styles.css: contiene estilos compartidos y del portfolio.

- blog/static/blog/styles.css: contiene estilos propios del blog.

- blog/migrations/: registra cambios en la estructura y las 
etiquetas de los datos guardados.

- blog/tests.py: contiene pruebas para comprobar las funciones principales del blog.

- media/: es la carpeta configurada para guardar archivos multimedia que se suben a traves de formularios.

