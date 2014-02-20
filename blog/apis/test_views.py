from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
import httplib2
from instagram.client import InstagramAPI
import oauth2 as oauth
import json
from django.shortcuts import render, get_object_or_404
from .models import ApiLink, FoursquareCheckin


def test_twitter(request):
    """
    Testpage for twitter
    """
    api = get_object_or_404(ApiLink, name="Twitter")
    consumer = oauth.Consumer(key=api.api_key, secret=api.api_secret)
    access_token = oauth.Token(key=api.access_token, secret=api.access_token_secret)
    client = oauth.Client(consumer, access_token)

    resp, content = client.request('https://api.twitter.com/1.1/statuses/user_timeline.json', 'GET')
    data = json.loads(content)

    tweet_list = []
    for tweet in data:
        tweet_list.append(tweet)

    return render(request, 'apis/api_test.html', {
        'data': tweet_list,
    })


def test_instagram(request):
    """
    Testpage for instagram
    Get access token manually first,
    see https://github.com/Instagram/python-instagram/blob/master/get_access_token.py
    Got mine through http://www.blueprintinteractive.com/tutorials/instagram/uri.php?code=71520761ada343ef882abb5c7a54a9fd
    """
    api = get_object_or_404(ApiLink, name="Instagram")


    instagram = InstagramAPI(access_token=api.access_token)
    #Access token secret = user_id!
    recent_media, next = instagram.user_recent_media(user_id=api.access_token_secret, count=10)

    photos = []
    for media in recent_media:
        direc = dir(media)
        photos.append('<img src="%s" />' % media.images['thumbnail'].url)
        #Check if media is video or image
        media_type = 'pic' if media.type == "image" else "vid"


    return render(request, 'apis/api_instagram.html', {
        'content': recent_media,
    })


def test_strava(request):
    """
    Testpage for Strava
    id: 293943
    """
    api = get_object_or_404(ApiLink, name="Strava")
    if not api.access_token:
        redirect_uri = settings.BASE_URL + api.callback_url
        return HttpResponseRedirect('https://www.strava.com/oauth/authorize?client_id=%(client)s&response_type=code&redirect_uri=%(redirect)s&scope=view_private' % {
            'client': api.api_key,
            'redirect': redirect_uri,
        })
    h = httplib2.Http()

    resp, content = h.request('https://www.strava.com/api/v3/athlete/activities?access_token=%s' % api.access_token)

    data = json.loads(content)

    return render(request, 'apis/api_strava.html', {
        'content': data,
    })


def callback_strava(request):
    api = get_object_or_404(ApiLink, name="Strava")
    code = request.GET.get('code', None)

    if code:
        h = httplib2.Http()
        resp, content = h.request(
            uri='https://www.strava.com/oauth/token?client_id=%(client_id)s&client_secret=%(secret)s&code=%(code)s' % {
            'client_id': api.api_key,
            'secret': api.api_secret,
            'code': code,
            },
            method="POST",
            headers={'Content-Type': 'application/json; charset=UTF-8'}
        )

        data = json.loads(content)

        try:
            api.access_token = data['access_token']
            api.save()
            messages.info(request, 'Geslaagd!')
        except KeyError:
            messages.info(request, 'Mislukt!')

    return HttpResponseRedirect(reverse('api_strava'))


def test_foursquare(request):
    """
    Testpage for foursquare
    """
    api = get_object_or_404(ApiLink, name="Foursquare")

    if not api.access_token:
        redirect_uri = settings.BASE_URL + api.callback_url
        return HttpResponseRedirect('https://foursquare.com/oauth2/authenticate?client_id=%(client)s&response_type=code&redirect_uri=%(redirect)s' % {
            'client': api.api_key,
            'redirect': redirect_uri,
        })

    h = httplib2.Http()

    resp, content = h.request('https://api.foursquare.com/v2/users/self/checkins?oauth_token=%(token)s&v=%(date)d' % {
        'token': api.access_token,
        'date': 20130214,
    })

    data = json.loads(content)
    data_type = type(data)
    del resp
    del content
    import datetime

    for checkin in data['response']['checkins']['items']:
        created = datetime.datetime.fromtimestamp(checkin['createdAt'])
        fs_model, created = FoursquareCheckin.objects.get_or_create(
            unique_url=checkin['id'],
            created=created,
            venue_lat=checkin['venue']['location']['lat'],
            venue_lng=checkin['venue']['location']['lng'],
        )
        fs_model.venue_name = checkin['venue']['name']
        fs_model.venue_url = checkin['venue']['id']
        try:
            fs_model.checkin_shout = checkin['shout']
        except KeyError:
            pass
        fs_model.save()

    return render(request, 'apis/api_foursquare.html', {
        'content': data['response']['checkins']['items'],
    })


def callback_foursquare(request):
    api = get_object_or_404(ApiLink, name="Foursquare")
    code = request.GET.get('code', None)

    if code:
        h = httplib2.Http()
        resp, content = h.request(
            uri='https://foursquare.com/oauth2/access_token?client_id=%(client)s&client_secret=%(secret)s&grant_type=authorization_code&redirect_uri=%(redirect)s&code=%(code)s' % {
                'client': api.api_key,
                'secret': api.api_secret,
                'redirect': settings.BASE_URL + request.path,
                'code': code,
            },
            method="POST",
            headers={'Content-Type': 'application/json; charset=UTF-8'}
        )

        data = json.loads(content)

        try:
            api.access_token = data['access_token']
            api.save()
            messages.success(request, 'Geslaagd!')
        except KeyError:
            messages.error(request, 'Fuck!')

    return HttpResponseRedirect(reverse('api_foursquare'))