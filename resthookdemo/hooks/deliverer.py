import requests
import json

from django.core import serializers


def deliver(target_url, payload, instance=None, hook=None):
    data = payload.get('data', {}).get('fields', {})
    requests.post(
        url=target_url,
        data=json.dumps(data, cls=serializers.json.DjangoJSONEncoder),
        headers={'Content-Type': 'application/json'},
    )
    return None
