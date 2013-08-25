from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_hooks.models import Hook


class BootstrapStyle(object):
    def __init__(self, *args, **kwargs):
        super(BootstrapStyle, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs = field.widget.attrs or {}
            field.widget.attrs.update({'class': 'form-control'})

class SignupForm(BootstrapStyle, forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(label='Password')

    def save(self, commit=True):
       user = super(SignupForm, self).save(commit=False)
       user.set_password(self.cleaned_data['password'])
       if commit:
           user.save()
       return user

    class Meta:
        model = User
        fields = ('username', )

class LoginForm(BootstrapStyle, forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def authenticate(self):
        return authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

class HookForm(BootstrapStyle, forms.ModelForm):
    class Meta:
        model = Hook
        fields = ('event', 'target')
