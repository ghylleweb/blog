from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.contrib import admin
from posts.models import BlogPost


class ApiLink(models.Model):
    """
    Store the endpoints here
    """
    name = models.CharField(max_length=75, unique=True)  # Eg. Facebook, Twitter, ...
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100, blank=True)
    access_token_secret = models.CharField(max_length=100, blank=True)
    callback_url = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name


class BaseSocialMedia(models.Model):
    """
    Fields that are the same across all kinds of social media posts
    """
    unique_url = models.URLField(unique=True)
    created = models.DateTimeField()

    class Meta:
        abstract = True


class FoursquareCheckin(BaseSocialMedia):
    """
    All the necessary info from a checkin
    Full list: https://developer.foursquare.com/docs/responses/checkin
    """
    venue_url = models.CharField(max_length=25)
    venue_name = models.CharField(max_length=75)
    venue_lat = models.FloatField()
    venue_lng = models.FloatField()
    checkin_shout = models.TextField(blank=True)

    blog_post = generic.GenericRelation(BlogPost)

    def __unicode__(self):
        return self.venue_name


class InstagramMedia(BaseSocialMedia):
    """
    All the necessary info from my media (video or image)
    Full list: http://instagram.com/developer/endpoints/media/
    """
    MEDIA_TYPES = (
        ('vid', 'video'),
        ('pic', 'image'),
    )
    media_type = models.CharField(choices=MEDIA_TYPES, max_length=3, default='pic')
    caption = models.TextField(blank=True)
    location_lat = models.FloatField(blank=True)
    location_lng = models.FloatField(blank=True)
    thumbnail = models.URLField()
    media_image = models.URLField()  # A video has a preview image
    video_url = models.URLField(blank=True)

    blog_post = generic.GenericRelation(BlogPost)


class StravaActivity(BaseSocialMedia):
    """
    All the necessary info from the activities on Strava
    Full list: http://strava.github.io/api/v3/activities/
    """
    ACTIVITY_TYPES = (
        ('C', 'cycle'),
        ('R', 'run'),
    )
    activity_type = models.CharField(choices=ACTIVITY_TYPES, max_length=1, default='C')
    avg_temp = models.FloatField()
    avg_speed = models.FloatField()
    #TODO uncertain which fields are important
    #TODO try to find the map

    blog_post = generic.GenericRelation(BlogPost)


class TwitterFeed(BaseSocialMedia):
    """
    Store my tweets
    Full list: https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline
    """
    tweet_text = models.TextField()
    tweet_lat = models.FloatField(blank=True)
    tweet_lng = models.FloatField(blank=True)

    blog_post = generic.GenericRelation(BlogPost)


admin.site.register(ApiLink)
admin.site.register(FoursquareCheckin)
admin.site.register(InstagramMedia)