from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author_name", "author_email", "body")
        widgets = {
            "author_name": forms.TextInput(attrs={"placeholder": "Tu nombre"}),
            "author_email": forms.EmailInput(attrs={"placeholder": "tu@email.com"}),
            "body": forms.Textarea(attrs={"placeholder": "Escribe tu comentario...", "rows": 5}),
        }
