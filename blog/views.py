from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Post

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    delete_error = None
    delete_form_open = False

    if request.method == "POST" and request.POST.get("action") == "delete_post":
        if request.POST.get("username") == ADMIN_USERNAME and request.POST.get("password") == ADMIN_PASSWORD:
            post.delete()
            return redirect("blog:list")
        delete_error = "El nombre de usuario o la contraseña son incorrectos."
        delete_form_open = True
        form = CommentForm()
    else:
        form = CommentForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f"{post.get_absolute_url()}#comentarios")

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "form": form,
            "delete_error": delete_error,
            "delete_form_open": delete_form_open,
        },
    )


def post_publish(request):
    if not request.session.get("can_publish_post"):
        if request.method == "POST":
            if (
                request.POST.get("username") == ADMIN_USERNAME
                and request.POST.get("password") == ADMIN_PASSWORD
            ):
                request.session["can_publish_post"] = True
                return redirect("blog:publish")
            return render(
                request,
                "blog/post_publish.html",
                {"auth_error": "El nombre de usuario o la contraseña son incorrectos."},
            )
        return render(request, "blog/post_publish.html")

    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save()
        request.session.pop("can_publish_post", None)
        return redirect(post.get_absolute_url())
    return render(request, "blog/post_publish.html", {"form": form})
