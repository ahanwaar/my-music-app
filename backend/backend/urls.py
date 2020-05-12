from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from graphene_django.views import GraphQLView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
   #  path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
