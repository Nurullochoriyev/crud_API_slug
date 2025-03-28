from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie_api/',movie_api),
    path('movie_detail/<slug:slug>/',movie_detail),
]
