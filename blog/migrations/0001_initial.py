from django.db import migrations, models
import django.db.models.deletion


def create_demo_posts(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    Post.objects.bulk_create([
        Post(
            title="Lo que estoy aprendiendo al construir con Django",
            slug="aprendiendo-a-construir-con-django",
            excerpt="Una primera nota sobre modelos, rutas y la tranquilidad de que cada pieza tenga un lugar.",
            content="Django me está ayudando a ordenar las ideas detrás de una web personal.\n\nEmpecé por separar el contenido de la presentación: los posts viven en la base de datos, mientras que las plantillas se ocupan de mostrar cada entrada. El panel de administración convierte esa separación en algo práctico: puedo publicar sin tocar el código.",
            media_url="assets/escamas.png",
        ),
        Post(
            title="Detrás de mis proyectos de juegos",
            slug="detras-de-mis-proyectos-de-juegos",
            excerpt="Lo que aprendí creando pequeños mundos, desde la lógica de juego hasta las pantallas que los hacen habitables.",
            content="Cada proyecto empieza con una idea bastante simple y termina enseñándome algo que no esperaba. Diseñar juegos me obliga a pensar en estados, decisiones y respuestas rápidas.\n\nTambién aprendí que una captura de pantalla puede contar mucho: por eso esta bitácora mezcla texto con imágenes y archivos multimedia.",
            media_url="assets/obamamenu.jpg",
        ),
    ])


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("slug", models.SlugField(unique=True)),
                ("excerpt", models.TextField(max_length=280)),
                ("content", models.TextField()),
                ("media", models.FileField(blank=True, upload_to="blog_media/")),
                ("media_url", models.CharField(blank=True, default="assets/escamas.png", max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "entrada",
                "verbose_name_plural": "entradas",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("author_name", models.CharField(max_length=80)),
                ("author_email", models.EmailField(max_length=254)),
                ("body", models.TextField(max_length=1000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("post", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="blog.post")),
            ],
            options={
                "verbose_name": "comentario",
                "verbose_name_plural": "comentarios",
                "ordering": ("created_at",),
            },
        ),
        migrations.RunPython(create_demo_posts, migrations.RunPython.noop),
    ]
