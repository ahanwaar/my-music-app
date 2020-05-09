from rest_framework import serializers
from .models import Artist, Album, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'album', 'artists')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'year', 'artist', )


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)
