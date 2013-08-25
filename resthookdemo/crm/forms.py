from django import forms

from resthookdemo.crm.models import Contact, Deal
from resthookdemo.forms import BootstrapStyle


class ContactForm(BootstrapStyle, forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email')

class DealForm(BootstrapStyle, forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('title', 'description', 'value')
