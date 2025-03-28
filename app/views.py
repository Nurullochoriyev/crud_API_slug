from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import MovieSerializers


# from serializers import *
@api_view(["get", "POST"])
def movie_api(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(["PUT","PATCH","DELETE"])
# def movie_detail(request,slug):
#
#     try:
#         movie=Movie.objects.get(slug=slug)
#         response={"success":True}
#     except Exception as e:
#         response["error"]=e
#         return Response(data=response,status=status.HTTP_417_EXPECTATION_FAILED)
#     if request.method=="GET":
#         serializer=MovieSerializers(movie)
#         response["data"]=serializer
#         return Response (data=response,status=status.HTTP_200_OK)
#     elif request.method=="PUT":
#         serializer=MovieSerializers(movie,data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             response["data"]=serializer
#             return Response(data=response,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializers

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail(request, slug):

    try:
        movie=Movie.objects.get(slug=slug)
        response={"success":True}
    except Exception as e:
        response["error"]=e
        return Response(data=response,status=status.HTTP_417_EXPECTATION_FAILED)
    # GET so'rov
    if request.method == "GET":
        serializer = MovieSerializers(movie)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    # PUT / PATCH so'rov
    elif request.method in ["PUT", "PATCH"]:
        partial = request.method == "PATCH"
        serializer = MovieSerializers(movie, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE so'rov
    elif request.method == "DELETE":
        movie.delete()
        return Response({"success": True, "message": "Movie deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

