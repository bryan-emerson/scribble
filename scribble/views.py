from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm

from .models import Post, Comment

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

def comment_create(request, primary_key):
    post = Post.objects.get(id = primary_key)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post_id = post.id
            form.save()
            return redirect('post_detail', primary_key)
    else:
        form = CommentForm()
        return render(request, 'comment_form.html', {'form': form, 'post': post})

def comment_delete(request, post_primary_key, primary_key):
    Comment.objects.get(id = primary_key).delete()
    return redirect('post_detail', post_primary_key)
