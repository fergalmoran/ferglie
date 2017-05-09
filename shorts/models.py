import random
import string

import logging
from django.conf import settings
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

"""
class User(AbstractUser):
    followers = models.ManyToManyField('self',
                                       related_name='followees',
                                       symmetrical=False)
"""


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Url(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_urls', null=True, blank=True)
    url = models.CharField(max_length=2048)
    shortened_url = models.CharField(max_length=6, unique=True)
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.url


@receiver(post_save, sender=Url, dispatch_uid="create_url_slug")
def create_url_slug(sender, instance, **kwargs):

    if instance.shortened_url:
        return

    chars = 'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    '0123456789'
    '_.-~'

    try:
        instance.shortened_url = get_random_string(4)  # create one
        found_slug = True
        while found_slug:  # keep checking until we have a valid slug
            found_slug = False
            other_objs_with_slug = type(instance).objects.filter(shortened_url=instance.shortened_url)
            if len(other_objs_with_slug) > 0:
                # if any other objects have current slug
                found_slug = True
            if found_slug:
                # create another slug and check it again
                instance.shortened_url = get_random_string(4, allowed_chars=chars)
        instance.save()
    except Exception as ex:
        logging.error(ex)
