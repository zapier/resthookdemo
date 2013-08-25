from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_hooks.models import Hook

from resthookdemo.forms import SignupForm, LoginForm, HookForm

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

@login_required
def edit_hook(request, hook_id=None):
    hook = None
    if hook_id:
        hooks = Hook.objects.filter(user=request.user)
        hook = get_object_or_404(hooks, id=hook_id)

    if request.method == 'POST':
        form = HookForm(request.POST, instance=hook)
        if form.is_valid():
            hook = form.save(commit=False)
            hook.user = request.user
            hook.save()
            return redirect('hooks_list')
    else:
        form = HookForm(instance=hook)

    return render(request, 'edit_hook.html', locals())

@login_required
def delete_hook(request, hook_id):
    hooks = Hook.objects.filter(user=request.user)
    hook = get_object_or_404(hooks, id=hook_id)
    hook.delete()
    return redirect('hooks_list')

