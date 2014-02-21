from django.conf.urls import patterns, url
from .views import BlogPostList, BlogPostDetail


urlpatterns = patterns(
    '',
    url(r'^$', BlogPostList.as_view(), name="posts_home"),
    url(r'^post/(?P<slug>\w+)/$', BlogPostDetail.as_view(), name="posts_detail"),
    )


