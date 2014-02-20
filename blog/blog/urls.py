from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from posts.views import BlogPostList

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', BlogPostList.as_view(), name='home'),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/ckeditor/', include('ckeditor.urls')),
    url(r'^grapelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^apis/', include('apis.urls')),
    url(r'^blog/', include('posts.urls')),
)
