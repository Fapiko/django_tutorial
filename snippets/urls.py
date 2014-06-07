from django.conf.urls import patterns, url

urlpatterns = patterns('snippets.views',
    url('^snippets/$', 'snippet_list'),
    url('^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail')
)
