from django.contrib.auth.models import User
from django.db import models
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)


class Contact(models.Model):
    """
    A root model for storing contacts, has a User owner.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey('auth.User')
    user = property(lambda s: s.owner)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return self.full_name


class Deal(models.Model):
    """
    Deals, because you want to make money. Has a contact (which has a User).
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey('auth.User')
    user = property(lambda s: s.owner)
    title = models.CharField(max_length=255)
    description = models.TextField()
    value = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return self.title
