from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'resthookdemo.hooks.views.hooks', name='hooks_list'),
    url(r'^create/$', 'resthookdemo.hooks.views.edit_hook', name='create_hook'),
    url(r'^history/$', 'resthookdemo.hooks.views.hook_history', name='hook_history_all'),
    url(r'^(?P<hook_id>\d+)/edit/$', 'resthookdemo.hooks.views.edit_hook', name='edit_hook'),
    url(r'^(?P<hook_id>\d+)/delete/$', 'resthookdemo.hooks.views.delete_hook', name='delete_hook'),
    url(r'^(?P<hook_id>\d+)/history/$', 'resthookdemo.hooks.views.hook_history', name='hook_history'),
)
