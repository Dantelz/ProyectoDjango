from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(f"{post.get_absolute_url()}#comentarios")
    return render(request, "blog/post_detail.html", {"post": post, "form": form})
