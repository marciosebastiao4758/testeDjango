from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "post_detail.html", {"post":post})
