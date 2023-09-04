from django.contrib.auth.models import Group
from rest_framework import serializers
from django.conf import settings
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class NewsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = '__all__'