from django import forms

from resthookdemo.crm.models import Contact, Deal


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email')

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('title', 'description', 'value')
