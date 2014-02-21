from django.conf.urls import patterns, url
from .views import BlogPostList, BlogPostDetail


urlpatterns = patterns(
    '',
    url(r'^$', BlogPostList.as_view(), name="posts_home"),
    url(r'^post/(?P<slug>.*)/$', BlogPostDetail.as_view(), name="posts_detail"),
    )


