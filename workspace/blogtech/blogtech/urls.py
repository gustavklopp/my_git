from django.conf.urls import patterns, include, url
from django.contrib import admin
from weblog import views
from weblog.views import PostList, PostDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.PostList, name='home'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
