from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form.cleaned_data['author'] = request.user
            form.instance.author = request.user
            form.save()
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'posts/add_posts.html', {'form': form})


@login_required
def edit_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance = post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('homepage')
    return render(request, 'posts/add_posts.html', {'form': form})


@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('homepage')