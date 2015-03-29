from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dico_app.views.index.page', name='home'),
    url(r'^index$', 'dico_app.views.index.page', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<rcp_id>\d+)$', 'dico_app.views.dci_page.page', name='dci_page'),
    url(r'^dci_search$', 'dico_app.views.jsonview.dci_search', name='dci_search'),
    url(r'^spec_search$', 'dico_app.views.jsonview.spec_search', name='spec_search'),

    url(r'^admin/', include(admin.site.urls)),
)
