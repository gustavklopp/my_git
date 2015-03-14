from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'RCP_website.views.index.page'),
    url(r'^index$', 'RCP_website.views.index.page', name="public_index"),
    url(r'^connection$', 'RCP_website.views.connection.page', name="public_connection")

#     url(r'^admin/', include(admin.site.urls)),
)
