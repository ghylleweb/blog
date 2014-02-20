from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_edit = models.DateTimeField(auto_now=True)
    visible_until = models.DateTimeField(blank=True, null=True)

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(db_index=True, blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title
