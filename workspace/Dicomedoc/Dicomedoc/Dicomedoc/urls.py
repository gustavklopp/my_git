from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dico_app.views.index.page', name='home'),
    url(r'^index$', 'dico_app.views.index.page', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dci_page$', 'dico_app.views.dci_page.page', name='dci_page'),

    url(r'^admin/', include(admin.site.urls)),
)
