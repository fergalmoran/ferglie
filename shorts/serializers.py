from rest_framework import serializers
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
    shortened_url = serializers.Field(source='shorten_url')

    class Meta:
        model = Url
