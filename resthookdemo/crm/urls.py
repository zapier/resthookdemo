from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^contacts$', 'resthookdemo.crm.views.contacts', name='contacts_list'),
    url(r'^contacts/create$', 'resthookdemo.crm.views.edit_contact', name='create_contact'),
    url(r'^contacts/(?P<contact_id>\d+)/edit$', 'resthookdemo.crm.views.edit_contact', name='edit_contact'),
    url(r'^contacts/(?P<contact_id>\d+)/delete$', 'resthookdemo.crm.views.delete_contact', name='delete_contact'),

    url(r'^deals$', 'resthookdemo.crm.views.deals', name='deals_list'),
    url(r'^deals/create$', 'resthookdemo.crm.views.edit_deal', name='create_deal'),
    url(r'^deals/(?P<deal_id>\d+)/edit$', 'resthookdemo.crm.views.edit_deal', name='edit_deal'),
    url(r'^deals/(?P<deal_id>\d+)/delete$', 'resthookdemo.crm.views.delete_deal', name='delete_deal'),
)
