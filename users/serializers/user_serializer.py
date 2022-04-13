<<<<<<< HEAD:users/serializers.py
from profiles.serializers import PhotosSerializer, StatusSerializer
from users.models import CustomUser
=======
>>>>>>> github/main:users/serializers/user_serializer.py
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

<<<<<<< HEAD:users/serializers.py

class UserSerializer(serializers.ModelSerializer):
=======
from follows.models.follow import Follow
from users.models import CustomUser
from common.base_serializer import BaseSerializer


class UserSerializer(BaseSerializer):
>>>>>>> github/main:users/serializers/user_serializer.py
    name = serializers.CharField(source='first_name')

    photos = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    followed = serializers.SerializerMethodField()

<<<<<<< HEAD:users/serializers.py
    def get_photos(self, user):
        # profile = user.profile_set.first()
        photos = user.profile.photos
        return PhotosSerializer(photos).data

    def get_status(self, user):
        profile = user.profile
        return StatusSerializer(profile).data
=======
    permission_classes = [IsAuthenticated]
>>>>>>> github/main:users/serializers/user_serializer.py

    def get_followed(self, user):
        me = self.context['request'].user

        if me.is_anonymous:
            return False

        return Follow.objects.filter(follower=me, followed=user).exists()

    class Meta:
        model = CustomUser
<<<<<<< HEAD:users/serializers.py
        fields = ['id', 'name', 'photos', 'status', 'followed']
=======
        fields = ['id', 'username', 'email', 'name', 'first_name', 'last_name', 'followed']
>>>>>>> github/main:users/serializers/user_serializer.py
