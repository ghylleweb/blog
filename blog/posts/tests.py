import datetime

from django.test import TestCase
from .models import BlogPost


# Create your tests here.
class BlogPostTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(
            id=1,
            title='Starting up my Blog',
            date_created=datetime.datetime.now(),
            text='Tekst',
            )
