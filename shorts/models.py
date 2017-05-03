from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from core import url

"""
class User(AbstractUser):
    followers = models.ManyToManyField('self',
                                       related_name='followees',
                                       symmetrical=False)
"""


class Url(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_urls', null=True, blank=True)
    url = models.CharField(max_length=2048)
    shortened_url = models.CharField(max_length=6)
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.url

    def shorten_url(self):
        return "%s%s" % (settings.STATIC_URL, url.dehydrate(self.id))
