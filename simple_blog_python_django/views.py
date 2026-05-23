from django.shortcuts import render
from posts.models import Post

def homepage(request):
    data = Post.objects.all()
    return render(request, 'homepage.html', {'data': data}) 