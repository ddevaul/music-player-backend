from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path('playlists/', views.PlaylistList.as_view()),
    path('curatedplaylists/', views.CuratedPlaylistList.as_view()),
    path('artists/', views.ArtistList.as_view()),
    path('songs/', views.SongList.as_view()),
    path('albums/', views.AlbumList.as_view()),
    path('songs/song/songbyname/<songname>/', views.SongByName.as_view()),
    path('songs/song/<int:pk>/', views.SongDetail.as_view()),
    path('songwrappers/songwrapper/<int:pk>/', views.PlaylistSongDetail.as_view()),
    path('albums/album/<int:pk>/', views.AlbumDetail.as_view()),
    path('artists/artist/<int:pk>/', views.ArtistDetail.as_view()),
    path('artists/artist/<int:artist>/essentials/', views.ArtistEssentials.as_view()),
    path('curatedplaylists/curatedplaylist/<int:pk>/', views.CuratedPlaylistDetail.as_view()),
    path('playlists/playlist/<int:pk>/', views.PlaylistDetail.as_view()),
    path('playlists/playlist/<int:playlist>/songs/', views.PlaylistSongs.as_view()),
]