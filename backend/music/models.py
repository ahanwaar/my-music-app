from django.db import models


class Artist(models.Model):
    """Database model for the Artists"""
    name = models.CharField('Name', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name


class Album(models.Model):
    """Database model for the Albums"""
    title = models.CharField('Album Title', max_length=50)
    # many albums can be related to the same artist
    year = models.PositiveIntegerField('Year')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.title


class Song(models.Model):
    """Database model for the Songs"""
    title = models.CharField('Song', max_length=50);
    # many songs can be related to the same album
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    # many artists can sing the same song
    artists = models.ManyToManyField(Artist)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.title
