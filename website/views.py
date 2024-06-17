from django.shortcuts import render
from .models import Post, Contact

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "post_detail.html", {"post":post})

def save_form(request):
    # print(request.POST)
    name = request.POST["name"]
    Contact.objects.create(
        name = name,
        email = request.POST["email"],
        message = request.POST["message"]
    )
    return render(request, "contact_sucess.html", {"name":name})
