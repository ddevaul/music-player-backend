from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Artist(models.Model):
  name = models.CharField(max_length=60)
  def __str__(self):
      return self.name


class Playlist(models.Model):
  class PlaylistType(models.TextChoices):
        Album = 'Album', _('Album')
        Playlist = 'Playlist', _('Playlist')
        CuratedPlaylist = 'CuratedPlaylist', _('CuratedPlaylist')

  playlist_type = models.CharField(
      max_length=20,
      choices=PlaylistType.choices,
      default=PlaylistType.Playlist,
    )
  name = models.CharField(max_length=60)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
  img_url = models.CharField(max_length=100, blank=True, null=True)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
  def __str__(self):
      return self.name

class Song(models.Model):
  name = models.CharField(max_length=60)
  url = models.CharField(max_length=100)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
  album = models.ForeignKey(Playlist, on_delete=models.CASCADE)
  def __str__(self):
      return self.name

class OrderedPlaylistSong(models.Model):
  song = models.ForeignKey(Song, on_delete=models.CASCADE)
  order = models.IntegerField()
  playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
