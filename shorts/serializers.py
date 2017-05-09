from rest_framework import serializers

from shortio import settings
from .models import Url

"""
class UserSerializer(serializers.ModelSerializer):
    urls = serializers.HyperlinkedIdentityField(
        'user_urls',
        lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'user_urls', )
"""


class UrlSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    shortened_url = serializers.SerializerMethodField()

    class Meta:
        model = Url
        fields = ('user', 'url', 'shortened_url', 'date_created')

    def get_shortened_url(self, instance):
        return "{}{}".format(settings.ROOT_DISPATCHER_URL, instance.shortened_url)
