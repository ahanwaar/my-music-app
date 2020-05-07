from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import  Artist, Album, Song
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer


def get_song_options():
    return "options", {
        "song": [{'label': obj.name, 'value': obj.pk} for obj in Song.objects.all()],
    }

def get_album_options():
    return "options", {
        "album": [{'label': obj.name, 'value': obj.pk} for obj in Album.objects.all()],
    }

def get_artist_options():
    return "options", {
        "artist": [{'label': obj.name, 'value': obj.pk} for obj in Artist.objects.all()],
    }


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer

    def get_options(self):
        return get_song_options()

    class Meta:
        datatables_extra_json = ('get_options', )


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('year')
    serializer_class = AlbumSerializer

    def get_options(self):
        return get_album_options()

    class Meta:
        datatables_extra_json = ('get_options', )


class ArtistViewSet(viewsets.ViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def get_options(self):
        return get_artist_options()

    class Meta:
        datatables_extra_json = ('get_options', )
