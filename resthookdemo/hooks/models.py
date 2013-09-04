from django.db import models
from django.dispatch import receiver

from rest_hooks.signals import hook_sent_event


class HookHistory(models.Model):
    """
    A root model for storing delivered hooks, has a Hook
    """
    sent_date = models.DateTimeField(auto_now_add=True)

    payload = models.CharField(max_length=2048)
    hook = models.ForeignKey('rest_hooks.Hook')

    def __unicode__(self):
        return self.id

@receiver(hook_sent_event)
def sent_hook_handler(sender, payload, instance, hook, **kwargs):
    history = HookHistory(payload=payload, hook=hook)
    history.save()
    return None
