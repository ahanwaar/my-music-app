from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from music import views

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet, 'songs')
router.register(r'albums', views.AlbumViewSet, 'albums')
router.register(r'artists', views.ArtistViewSet, 'artists')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
