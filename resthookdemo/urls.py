from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from resthookdemo.crm.api import ContactResource, DealResource, HookResource

v1_api = Api(api_name='v1')
v1_api.register(ContactResource())
v1_api.register(DealResource())
v1_api.register(HookResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'resthookdemo.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crm/', include('resthookdemo.crm.urls')),
    url(r'^api/', include(v1_api.urls)),
)
