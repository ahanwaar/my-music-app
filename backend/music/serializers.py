from rest_framework import serializers
from music.models import  Artist, Album, Song

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('name','bio')


class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.ReadOnlyField(source='artist.name')
    artist = ArtistSerializer()

    DT_RowId = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()

    def get_DT_RowId(self, album):
        return 'row_%d' % album.pk

    def get_DT_RowAttr(self, album):
        return {'data-pk': album.pk}

    class Meta:
        model = Album
        fields = (
            'DT_RowId', 'DT_RowAttr', 'name',
            'year', 'artist_name', 'artist',
        )


class SongSerializer(serializers.ModelSerializer):
    album_name = serializers.ReadOnlyField(source='album.name')
    album = AlbumSerializer()

    DT_RowId = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()

    def get_DT_RowId(self, song):
        return 'row_%d' % song.pk

    def get_DT_RowAttr(self, song):
        return {'data-pk': song.pk}


    class Meta:
        model = Song
        fields = (
            'DT_RowId', 'DT_RowAttr', 'name',
             'album_name', 'album',
        )
