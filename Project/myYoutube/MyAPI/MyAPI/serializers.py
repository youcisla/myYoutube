from rest_framework import serializers
from .models import MyUser
from MyAPI.models import Video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'username', 'is_staff','pseudo', 'password')
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ( 'username','pseudo', 'email', 'password')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ( "name", "source")
        
