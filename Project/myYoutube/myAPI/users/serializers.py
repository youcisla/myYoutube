from rest_framework import serializers

from .models import Comment, User, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'pseudo', 'email', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            pseudo=validated_data.get('pseudo', validated_data['username'])
        )
        return user

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'name', 'source', 'user']
        read_only_fields = ['id', 'user']

    def validate(self, data):
        if not data.get('name') or not data.get('source'):
            raise serializers.ValidationError("Both 'name' and 'source' fields are required.")
        return data
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video', 'user', 'body', 'created_at']
        read_only_fields = ['id', 'video', 'user', 'created_at']