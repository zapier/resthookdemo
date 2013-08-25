from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def save(self, commit=True):
       user = super(SignupForm, self).save(commit=False)
       user.set_password(self.cleaned_data['password'])
       if commit:
           user.save()
       return user

    class Meta:
        model = User
        fields = ('username', )

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def authenticate(self):
        return authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
