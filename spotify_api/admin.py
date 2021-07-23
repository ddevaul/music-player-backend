from django.contrib import admin
from .models import (Playlist, Song, OrderedPlaylistSong, Artist)

# Register your models here.
admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(OrderedPlaylistSong)
admin.site.register(Artist)