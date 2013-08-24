from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^contacts$', 'resthookdemo.crm.views.contacts', name='contacts_list'),
    url(r'^deals$', 'resthookdemo.crm.views.deals', name='deals_list'),
    url(r'^contacts/(?P<contact_id>[\d]+)/deals$', 'resthookdemo.crm.views.deals', name='deals_for_contact'),
)
