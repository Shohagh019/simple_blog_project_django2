from django.shortcuts import render, redirect
from . import forms
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Registration successful!')
            return redirect('homepage')
            
    else:                                               
        registration_form = forms.RegistrationForm()
    return render(request, 'authors/registration.html', {'form': registration_form, 'title': 'Register'})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')

    else:
        form = AuthenticationForm()
    return render(request, 'authors/registration.html', {'form': form, 'title': 'Login'})


@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = forms.EditProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('homepage')
    else:
        profile_form = forms.EditProfileForm(instance=request.user)
    return render(request, 'authors/profile_update.html', {'form': profile_form, 'title': 'Update Profile'})

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password updated successfully!')
            return redirect('profile_update')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authors/password_change.html', {'form': form})