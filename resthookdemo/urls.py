import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from resthookdemo.crm.api import ContactResource, DealResource, HookResource


admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ContactResource())
v1_api.register(DealResource())
v1_api.register(HookResource())

urlpatterns = patterns('',
    # url(r'^$', 'resthookdemo.views.home', name='home'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

    url(r'^$', 'resthookdemo.views.home', name='home'),
    url(r'^signup$', 'resthookdemo.views.signup', name='signup'),
    url(r'^login$', 'resthookdemo.views.do_login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crm/', include('resthookdemo.crm.urls')),
    url(r'^api/', include(v1_api.urls)),
)
