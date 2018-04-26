from django.shortcuts import render, redirect
from .forms import PostForm

from .models import Post

def post_list(request):
    posts = list(Post.objects.all())
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, primary_key):
    post = Post.objects.get(id = primary_key)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save()
            return redirect('post_detail', primary_key = post.id)
    else:
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})

def post_update(request, primary_key):
    post = Post.objects.get(id = primary_key)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid:
            post = form.save()
            return redirect('post_detail', primary_key = post.id)
    else:
        form = PostForm(instance = post)
        return render(request, 'post_form.html', {'form': form})

def post_delete(request, primary_key):
    Post.objects.get(id = primary_key).delete()
    return redirect('post_list')
