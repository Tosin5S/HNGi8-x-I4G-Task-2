from django.shortcuts import render

from resume_page.forms import CommentForm
from resume_page.models import Post, Comment


# Create your views here.

def resume_page(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "resume_page.html", context)
