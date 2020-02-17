from rest_framework import serializers
from .models import Photo


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('imageFile', 'caption', 'pubDate', 'user', 'status')
