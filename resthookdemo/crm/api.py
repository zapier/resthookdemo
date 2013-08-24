from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization

from rest_hooks.models import Hook
from resthookdemo.crm.models import Contact, Deal


class ContactResource(ModelResource):

    def obj_create(self, bundle, request=None, **kwargs):
        return super(ContactResource, self).obj_create(bundle,
                                                    request,
                                                    owner=request.user)

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(owner=request.user)

    class Meta:
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        queryset = Contact.objects.all()
        resource_name = 'contacts'

class DealResource(ModelResource):
    def obj_create(self, bundle, request=None, **kwargs):
        return super(DealResource, self).obj_create(bundle,
                                                    request,
                                                    owner=request.user)

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(contact__owner=request.user)

    class Meta:
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        queryset = Deal.objects.all()
        resource_name = 'deals'

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
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete']
        fields = ['event', 'target']
