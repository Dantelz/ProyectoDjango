from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author_name", "author_email", "body")
        widgets = {
            "author_name": forms.TextInput(attrs={"placeholder": "Tu nombre"}),
            "author_email": forms.EmailInput(attrs={"placeholder": "tu@email.com"}),
            "body": forms.Textarea(attrs={"placeholder": "Escribe tu comentario...", "rows": 5}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "slug", "excerpt", "content", "media", "media_url")
        widgets = {
            "excerpt": forms.Textarea(attrs={"rows": 3}),
            "content": forms.Textarea(attrs={"rows": 8}),
        }
