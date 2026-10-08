from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField("Título", max_length=160)
    slug = models.SlugField("Identificador URL", unique=True)
    excerpt = models.TextField("Resumen", max_length=280)
    content = models.TextField("Contenido")
    media = models.FileField("Archivo multimedia", upload_to="blog_media/", blank=True)
    media_url = models.CharField(
        "Ruta de imagen estática",
        max_length=255,
        blank=True,
        default="assets/escamas.png",
    )
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última modificación", auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Entrada",
    )
    author_name = models.CharField("Nombre", max_length=80)
    author_email = models.EmailField("Correo electrónico")
    body = models.TextField("Comentario", max_length=1000)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"

    def __str__(self):
        return f"{self.author_name} en {self.post.title}"
