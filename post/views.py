from django.shortcuts import render
from post.models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def post(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post.html',{'post':post})
