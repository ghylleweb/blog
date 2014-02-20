from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apis.test_views',
    url(r'^foursquare/$', 'test_foursquare', name="api_foursquare"),
    url(r'^instagram/$', 'test_instagram', name="api_instagram"),
    url(r'^strava/$', 'test_strava', name="api_strava"),
    url(r'^twitter/$', 'test_twitter', name="api_twitter"),
    url(r'^callback/foursquare/$', 'callback_foursquare', name="api_callback_foursquare"),
    url(r'^callback/strava/$', 'callback_strava', name="api_callback_strava"),
)