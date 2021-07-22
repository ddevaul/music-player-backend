from rest_framework import serializers
from .models import (Playlist, Artist, Song, OrderedPlaylistSong)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'id',)

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('name', 'url', 'artist', 'id', 'album')
        depth = 1

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('name', 'owner', 'playlist_type', 'id', 'img_url')

class OrderedPlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedPlaylistSong
        fields = ('song', 'order', 'playlist','id',)
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['song'] = SongSerializer(instance.song).data
        response['playlist'] = PlaylistSerializer(instance.playlist).data
        return response


# class OrderedAlbumSongSerializer(serializers.ModelSerializer):
#     song = SongSerializer()
#     class Meta:
#         model = OrderedAlbumSong
#         fields = ('song', 'order', 'album','id',)
#         depth = 2
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['song'] = SongSerializer(instance.song).data
#         return response


        
