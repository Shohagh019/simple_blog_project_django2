from django.urls import path
from posts.views import add_posts, edit_post, delete_post

urlpatterns = [
    path('add/', add_posts, name='add_posts'),
    path('edit/<int:id>/', edit_post, name='edit_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),
]