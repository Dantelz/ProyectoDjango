from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=280)
    content = models.TextField()
    media = models.FileField(upload_to="blog_media/", blank=True)
    media_url = models.CharField(max_length=255, blank=True, default="assets/escamas.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=80)
    author_email = models.EmailField()
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"

    def __str__(self):
        return f"{self.author_name} en {self.post.title}"
