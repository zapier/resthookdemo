from resthookdemo.forms import BootstrapStyle

from django import forms

from rest_hooks.models import Hook


class HookForm(BootstrapStyle, forms.ModelForm):
    class Meta:
        model = Hook
        fields = ('event', 'target')
