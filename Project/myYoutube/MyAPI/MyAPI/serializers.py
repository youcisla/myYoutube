from django.conf import settings
from rest_framework import serializers

from .models import MyUser, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'username', 'is_staff','pseudo', 'password')
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ( 'username','pseudo', 'email', 'password')

class VideoSerializer(serializers.ModelSerializer):
    source_url = serializers.SerializerMethodField()

    def get_source_url(self, obj):
        # Ensure proper URL construction
        request = self.context.get('request')
        if obj.source:
            return request.build_absolute_uri(obj.source.url)  # Build absolute URL
        return None

    class Meta:
        model = Video
        fields = ("id", "name", "source", "source_url")
