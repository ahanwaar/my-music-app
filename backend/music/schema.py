import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Artist, Album, Song


class SongType(DjangoObjectType):
    class Meta:
        model = Song


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist

    def resolve_artist_poster(self, info):
         return self.artist_poster

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album

    def resolve_album_poster(self, info):
         return self.album_poster


class Query(ObjectType):
    artist = graphene.Field(ArtistType, id=graphene.Int())
    album = graphene.Field(AlbumType, id=graphene.Int())
    song = graphene.Field(SongType, id=graphene.Int())
    artists = graphene.List(ArtistType)
    albums = graphene.List(AlbumType)
    songs = graphene.List(SongType)

    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Artist.objects.get(pk=id)

        return None

    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Song.objects.get(pk=id)

        return None

    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Album.objects.get(pk=id)

        return None

    def resolve_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_songs(self, info, **kwargs):
        return Song.objects.all()

    def resolve_albums(self, info, **kwargs):
        return Album.objects.all()


schema = graphene.Schema(query=Query)