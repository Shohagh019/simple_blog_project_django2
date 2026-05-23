from django.shortcuts import render, redirect
from . import forms
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('homepage')
            
    else:                                               
        registration_form = forms.RegistrationForm()
    return render(request, 'authors/registration.html', {'form': registration_form})
