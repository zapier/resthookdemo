from django.contrib.auth.models import User
from django.db import models

from tastypie.models import create_api_key


class Contact(models.Model):
    """
    A root model for storing contacts, has a User user.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth.User')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return self.full_name


class Deal(models.Model):
    """
    Deals, because you want to make money. Has a User).
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    description = models.TextField()
    value = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return self.title


def create_some_fixtures(sender, instance, created, **kwargs):
    import names
    import random

    if not created:
        return

    for x in range(5):
        first = names.get_first_name()
        last = names.get_last_name()
        full_name = u'{} {}'.format(first, last)
        email = u'{}@example.com'.format(first.lower().strip())
        Contact.objects.create(user=instance,
                               full_name=full_name,
                               email=email)

        adj = random.choice(['crazy', 'black', 'fancy',
                               'sneaky', 'giant', 'spicy'])
        thing = random.choice(['shoe', 'cat', 'lamp',
                               'car', 'parrot', 'burrito'])
        title = u'{} wants a {} {}'.format(first, adj, thing)
        description = 'This is not a very good description is it?'
        Deal.objects.create(user=instance,
                            title=title,
                            description=description,
                            value=random.random() * 100)
models.signals.post_save.connect(create_some_fixtures, sender=User)

models.signals.post_save.connect(create_api_key, sender=User)
