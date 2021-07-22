from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import Http404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from .serializers import (PlaylistSerializer, ArtistSerializer, 
SongSerializer, OrderedPlaylistSongSerializer)
from .models import Playlist, Artist, Song, OrderedPlaylistSong

class AdminWriteOrReadOnly(BasePermission):
    message = 'Editing restricted to admins'
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser

class IsOwnerOrAdminOtherwiseReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user or request.user.is_superuser


class PlaylistList(generics.ListCreateAPIView, IsOwnerOrAdminOtherwiseReadOnly):
    permission_classes = [IsOwnerOrAdminOtherwiseReadOnly]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get(self, request, format=None):
        playlists = Playlist.objects.filter(owner=request.user, playlist_type='Playlist')
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CuratedPlaylistList(generics.ListCreateAPIView, AdminWriteOrReadOnly):
    permission_classes = [AdminWriteOrReadOnly]
    queryset = Playlist.objects.filter(playlist_type='CuratedPlaylist')
    serializer_class = PlaylistSerializer
    # def get(self, request, format=None):
    #     curatedplaylists = CuratedPlaylist.objects.filter()
    #     serializer = CuratedPlaylistSerializer(curatedplaylists, many=True)
    #     return Response(serializer.data)

class SongList(generics.ListCreateAPIView, AdminWriteOrReadOnly):
    permission_classes = [AdminWriteOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # def get(self, request, format=None):
    #     songs = Song.objects.all()
    #     serializer = SongSerializer(songs, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SongSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumList(generics.ListCreateAPIView, AdminWriteOrReadOnly):
    permission_classes = [AdminWriteOrReadOnly]
    queryset = Playlist.objects.filter(playlist_type='Album')
    serializer_class = PlaylistSerializer
    # def get(self, request, format=None):
    #     albums = Album.objects.all()
    #     serializer = AlbumSerializer(albums, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = AlbumSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistList(generics.ListCreateAPIView, AdminWriteOrReadOnly):
    permission_classes = [AdminWriteOrReadOnly]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # def get(self, request, format=None):
    #     artists = Artist.objects.all()
    #     serializer = ArtistSerializer(artists, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = ArtistSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetail(generics.RetrieveUpdateDestroyAPIView, AdminWriteOrReadOnly):
    permission_classes = [AdminWriteOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    """
    Retrieve, update or delete a snippet instance.
    """
    # def get_object(self, pk):
    #     try:
    #         return Song.objects.get(pk=pk)
    #     except Song.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     song = self.get_object(pk)
    #     serializer = SongSerializer(song)
    #     return Response(serializer.data)

class SongByName(generics.RetrieveAPIView, AdminWriteOrReadOnly):
    def get_object(self, songname):
        try:
            return Song.objects.filter(name=songname)
        except Song.DoesNotExist:
            raise Http404

    # def post(self, req, format=None):
    #     songs = self.get_object(req)
    #     serializer = SongSerializer(songs, many=True)
    #     return Response(serializer.data)

    def get(self, request, songname, format=None):
        songs = self.get_object(songname)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = ArtistSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView, AdminWriteOrReadOnly):
    permission_classes = [AdminWriteOrReadOnly]
    queryset = Playlist.objects.filter(playlist_type='Album')
    serializer_class = PlaylistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView, AdminWriteOrReadOnly):
    # permission_classes = [AdminWriteOrReadOnly]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView, IsOwnerOrAdminOtherwiseReadOnly):
    permission_classes = [IsOwnerOrAdminOtherwiseReadOnly]
    queryset = Playlist.objects.filter(playlist_type='Playlist')
    serializer_class = PlaylistSerializer

class CuratedPlaylistDetail(generics.RetrieveUpdateDestroyAPIView, AdminWriteOrReadOnly):
    permission_classes = [AdminWriteOrReadOnly]
    queryset = Playlist.objects.filter(playlist_type='CuratedPlaylist')
    serializer_class = PlaylistSerializer

# rename this to SongWrappers or something like that 
class PlaylistSongs(APIView):
    def get_object(self, playlist):
        try:
            return OrderedPlaylistSong.objects.filter(playlist=playlist).order_by('order')
        except OrderedPlaylistSong.DoesNotExist:
            raise Http404

    def get(self, request, playlist, format=None):
        songs = self.get_object(playlist)
        serializer = OrderedPlaylistSongSerializer(songs, many=True)
        return Response(serializer.data)
    
    def post(self, request, playlist, format=None):
        serializer = OrderedPlaylistSongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistSongDetail(generics.RetrieveUpdateDestroyAPIView, AdminWriteOrReadOnly):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = OrderedPlaylistSong.objects.all()
    serializer_class = OrderedPlaylistSongSerializer

    

class ArtistSongs(APIView):
    def get_object(self, artist):
        try:
            return Song.objects.filter(artist=artist)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, artist, format=None):
        songs = self.get_object(artist)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

class ArtistEssentials(APIView):
    def get_object(self, artist):
        try:
            return Playlist.objects.filter(playlist_type='CuratedPlaylist').filter(artist=artist)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, artist, format=None):
        playlists = self.get_object(artist)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

