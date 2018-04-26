from django.shortcuts import render

from .models import Post

def post_list(request):
    posts = list(Post.objects.all())
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, primary_key):
    post = Post.objects.get(id=primary_key)
    return render(request, 'post_detail.html', {'post': post})
