from rest_framework import serializers

from profiles.models import Profile, Contacts, Photos


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['status']


class PostPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.first_name')
    contacts = ContactsSerializer()
    photos = PhotosSerializer()
    # photos = serializers.SerializerMethodField()

    # def get_photos(self, obj):
    #     serializer = PhotosSerializer(obj.user.photos)
    #     return serializer.data

    class Meta:
        model = Profile
        fields = '__all__'

