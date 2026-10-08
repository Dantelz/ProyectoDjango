from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Comment, Post


class PostDetailTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Post de prueba",
            slug="post-de-prueba",
            excerpt="Resumen",
            content="Contenido",
        )
        self.url = reverse("blog:detail", kwargs={"slug": self.post.slug})

    def test_delete_control_appears_before_post_title(self):
        response = self.client.get(self.url)
        content = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertLess(content.index('class="primary-button">Eliminar post'), content.index("<h1>"))
        self.assertContains(response, 'name="csrfmiddlewaretoken"')

    def test_delete_requires_admin_username_and_password(self):
        for credentials in (
            {"username": "otra-cuenta", "password": "admin"},
            {"username": "admin", "password": "incorrecta"},
        ):
            with self.subTest(credentials=credentials):
                response = self.client.post(
                    self.url,
                    {"action": "delete_post", **credentials},
                )

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, "El nombre de usuario o la contraseña son incorrectos.")
                self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())

    def test_correct_admin_credentials_delete_post(self):
        response = self.client.post(
            self.url,
            {"action": "delete_post", "username": "admin", "password": "admin"},
        )

        self.assertRedirects(response, reverse("blog:list"))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_comment_submission_still_works(self):
        response = self.client.post(
            self.url,
            {
                "author_name": "Visitante",
                "author_email": "visitante@example.com",
                "body": "Buen post",
            },
        )

        self.assertRedirects(response, f"{self.url}#comentarios")
        self.assertTrue(Comment.objects.filter(post=self.post, body="Buen post").exists())


class PostPublishingTests(TestCase):
    def setUp(self):
        self.url = reverse("blog:publish")

    def test_publish_page_requires_admin_credentials_before_showing_post_form(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nombre de usuario")
        self.assertNotContains(response, "Publicar una entrada")

    def test_invalid_credentials_do_not_grant_publish_access(self):
        response = self.client.post(
            self.url,
            {"username": "admin", "password": "incorrecta"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "El nombre de usuario o la contraseña son incorrectos.")
        self.assertNotIn("can_publish_post", self.client.session)

    def test_admin_credentials_allow_creating_a_post(self):
        response = self.client.post(
            self.url,
            {"username": "admin", "password": "admin"},
        )

        self.assertRedirects(response, self.url)
        form_response = self.client.get(self.url)
        self.assertContains(form_response, "Identificador URL")
        self.assertContains(form_response, "Resumen")
        self.assertContains(form_response, "Contenido")

        response = self.client.post(
            self.url,
            {
                "title": "Entrada nueva",
                "slug": "entrada-nueva",
                "excerpt": "Un resumen",
                "content": "El contenido de la entrada.",
                "media_url": "assets/escamas.png",
            },
        )

        post = Post.objects.get(slug="entrada-nueva")
        self.assertRedirects(response, post.get_absolute_url())
        self.assertNotIn("can_publish_post", self.client.session)

    def test_admin_add_entry_form_uses_spanish_field_labels(self):
        user = get_user_model().objects.create_superuser(
            username="superadmin",
            email="superadmin@example.com",
            password="test-password",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("admin:blog_post_add"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Identificador URL")
        self.assertContains(response, "Resumen")
        self.assertNotContains(response, ">Slug<")
        self.assertNotContains(response, ">Excerpt<")
