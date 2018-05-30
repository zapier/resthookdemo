import json

from django.conf.urls import url
from django.http import HttpResponse

from tastypie.authentication import SessionAuthentication, MultiAuthentication
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash

from resthookdemo.crm.api import PrettyJSONSerializer, UserObjectsOnlyAuthorization, ApiKeyAuthentication

from rest_hooks.models import Hook


class HookResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        bundle.data['target'] = bundle.data.pop('target_url', None)
        return super(HookResource, self).obj_create(bundle,
                                                    user=bundle.request.user)

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)

    class Meta:
        resource_name = 'hooks'
        queryset = Hook.objects.all()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        serializer = PrettyJSONSerializer()
        authorization = UserObjectsOnlyAuthorization()
        allowed_methods = ['get', 'post', 'delete']
        fields = ['event', 'target']
        default_format = 'application/json'

    def delete_hook(self, request, **kwargs):
        data = json.loads(request.body)
        if data:
            target_url = data.get('target_url')
            event = data.get('event')
            if target_url:
                Hook.objects.filter(target=target_url).delete()
            return HttpResponse('ok')
        return HttpResponse('skipped')

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/delete%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('delete_hook'), name='api_delete_hook'),
        ]
