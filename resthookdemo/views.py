from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_hooks.models import Hook

from resthookdemo.forms import SignupForm, LoginForm

def home(request):
    return render(request, 'base.html', locals())

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('contacts_list')
    else:
        form = SignupForm()
    return render(request, 'signup.html', locals())

def do_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
            if user:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return redirect('contacts_list')
            else:
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', locals())

@login_required
def hooks(request):
    user = request.user
    hooks = Hook.objects.filter(user=user)
    return render(request, 'hooks.html', locals())

