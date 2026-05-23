from django.urls import path
from authors.views import register

urlpatterns = [
    path('add/', register, name='register'),
]