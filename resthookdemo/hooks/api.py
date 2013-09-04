from tastypie.authentication import SessionAuthentication, MultiAuthentication
from tastypie.resources import ModelResource

from resthookdemo.crm.api import PrettyJSONSerializer, UserObjectsOnlyAuthorization, ApiKeyAuthentication

from rest_hooks.models import Hook


class HookResource(ModelResource):
    def obj_create(self, bundle, request=None, **kwargs):
        return super(HookResource, self).obj_create(bundle,
                                                    request,
                                                    user=request.user)

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
