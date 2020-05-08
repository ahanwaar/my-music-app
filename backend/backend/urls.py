from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import routers
from music.views import ArtistViewSet, SongViewSet, AlbumViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet, 'artists')
router.register(r'songs', SongViewSet, 'songs')
router.register(r'albums', AlbumViewSet, 'albums')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
