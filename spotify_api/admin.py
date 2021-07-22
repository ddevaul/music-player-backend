from django.contrib import admin
from .models import (Playlist, Song, OrderedPlaylistSong)

# Register your models here.
admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(OrderedPlaylistSong)



