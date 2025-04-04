


from app.views import *
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import  DefaultRouter
router=DefaultRouter()
router.register(r"actors",ActorApi)
router.register(r"movies",MovieApi)
# router.register(r"add",AddActorToMovieView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path('movi/<int:pk>/add-actor/', AddActorToMovieView.as_view(), name='add-actor-to-movie'),


    # path('movie_api/',movie_api),
    # path('movie_detail/<slug:slug>/',movie_detail),
    # path("ism_api/",ism_api),
    # path("movie/",MovieApi.as_view()),
    # path("movi/<int:pk>/",MovieDetail.as_view()),
]
