from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, NewPostForm
from .models import Post
from .models import Category, Post

# Create your views here.
def post_list(request) :
    posts = Post.objects.filter(end_date__gte=timezone.now()).order_by('end_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def category_list(request, pk) :
    posts = Post.objects.filter(category=pk).order_by('end_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request) :
    if request.method =="POST" :
        form = NewPostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.save()
            return redirect('post_new', pk=post.pk)
    else :
        form = NewPostForm()
    return render(request, 'blog/post_new.html', {'form' : form})

def post_edit(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    if request.method =="POST" :
        form = PostForm(request.POST, instance=post)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})