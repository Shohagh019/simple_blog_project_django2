from django.shortcuts import render
from categories.models import Category
from posts.models import Post

def homepage(request, category_slug = None):
    data = Post.objects.all()
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        data = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'homepage.html', {'data': data, 'categories': categories})