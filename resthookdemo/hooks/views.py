from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from rest_hooks.models import Hook

from resthookdemo.hooks.forms import HookForm
from resthookdemo.hooks.models import HookHistory


@login_required
def hooks(request):
    user = request.user
    hooks = Hook.objects.filter(user=user)
    return render(request, 'list.html', locals())

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

    return render(request, 'edit.html', locals())

@login_required
def delete_hook(request, hook_id):
    hooks = Hook.objects.filter(user=request.user)
    hook = get_object_or_404(hooks, id=hook_id)
    hook.delete()
    return redirect('hooks_list')

@login_required
def hook_history(request, hook_id):
    hooks = Hook.objects.filter(user=request.user)
    hook = get_object_or_404(hooks, id=hook_id)
    hook_history = HookHistory.objects.filter(hook=hook).order_by('-sent_date')
    return render(request, 'history.html', locals())
