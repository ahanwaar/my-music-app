from rest_framework.viewsets import ModelViewSet
from .models import Artist, Album, Song
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer

    def get_song_options(self):
        return "options", {
            "song": [{'label': obj.title, 'value': obj.pk} for obj in Song.objects.all()],
        }

    def get_options(self):
        return self.get_song_options()

    class Meta:
        datatables_extra_json = ('get_options',)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all().order_by('year')
    serializer_class = AlbumSerializer

    def get_album_options(self):
        return "options", {
            "album": [{'label': obj.title, 'value': obj.pk} for obj in Album.objects.all()],
        }

    def get_options(self):
        return self.get_album_options()

    class Meta:
        datatables_extra_json = ('get_options',)


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer

    def get_artist_options(self):
        return "options", {
            "artist": [{'label': obj.name, 'value': obj.pk} for obj in Artist.objects.all()],
        }

    def get_options(self):
        return self.get_artist_options()

    class Meta:
        datatables_extra_json = ('get_options',)
