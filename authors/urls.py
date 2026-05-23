from django.urls import path
from authors.views import register, user_login, profile_update, password_change, profile, user_logout

urlpatterns = [
    path('add/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('update_profile/', profile_update, name='update_profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('update_profile/password_change/', password_change, name='password_change'),
]