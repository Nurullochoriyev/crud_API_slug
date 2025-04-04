from http.client import responses

from django.shortcuts import render


from rest_framework import generics, status




from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import MovieSerializers, ActorsSerializer




class ActorApi(ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer



class MovieApi(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers



class AddActorToMovieView(generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    def post(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')

        if not actor_id:
            return Response(
                {"error": "Actor ID ko'rsatilmagan"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            actor = Actors.objects.get(id=actor_id)
        except Actors.DoesNotExist:
            return Response(
                {"error": "Bunday aktyor topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        if movie.actors.filter(id=actor_id).exists():
            return Response(
                {"error": "Bu aktyor allaqachon kinoga qo'shilgan"},
                status=status.HTTP_400_BAD_REQUEST
            )

        movie.actors.add(actor)
        serializer = self.get_serializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


#








# class MovieApi(APIView):
#     def get(self, request):
#         movie=Movie.objects.all()
#         serializer=MovieSerializers(movie,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         data={"success":True}
#         serializer=MovieSerializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=data)
#         data["success"]=False
#         return Response(data=data)
#
#
#
# class   MovieDetail(APIView):
#     def get(self,request,pk):
#         response={"success":True}
#         try:
#             movie=Movie.objects.get(pk=pk)
#             serializer=MovieSerializers(movie)
#             response["data"]=serializer.data
#             return Response(data=response)
#         except Movie.DoesNotExist:
#             response["success"]=False
#             return Response(data=response)
#     def put(self, request,pk):
#         response={"success":True}
#         try:
#             movie=Movie.objects.get(pk=pk)
#             serializer=MovieSerializers(movie)
#             response["data"]=serializer.data
#             return Response(data=response)
#         except Movie.DoesNotExist:
#             response['success']=False
#             return Response(data=response)
#
# class ActorApi(APIView):
#     def get(self,request):
#         actor=Actors.objects.all()
#         serializer=ActorsSerializer(actor,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         data={"success":True}
#         serializer=ActorsSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=data)
#         data['success']=False
#         return Response(data=data)
# class ActorDetail(APIView):
#     def get(self,request,pk):
#         response={"success":True}
#         try:
#             actor=Actors.objects.get(pk=pk)
#             serializer=ActorsSerializer(actor)
#             response["data"]=serializer.data
#             return Response(data=response)
#         except Actors.DoesNotExist:
#             response["success"] = False
#             return Response(data=response)
#
#
#     def put(self, request, pk):
#         response = {"success": True}
#         try:
#             actor = Actors.objects.get(pk=pk)
#             serializer = ActorsSerializer(actor)
#             response["data"] = serializer.data
#             return Response(data=response)
#         except Actors.DoesNotExist:
#             response['success'] = False
#             return Response(data=response)
#
#




























# from serializers import *
# @api_view(["get", "POST"])
# def movie_api(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     if request.method == "POST":
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # @api_view(["PUT","PATCH","DELETE"])
# # def movie_detail(request,slug):
# #
# #     try:
# #         movie=Movie.objects.get(slug=slug)
# #         response={"success":True}
# #     except Exception as e:
# #         response["error"]=e
# #         return Response(data=response,status=status.HTTP_417_EXPECTATION_FAILED)
# #     if request.method=="GET":
# #         serializer=MovieSerializers(movie)
# #         response["data"]=serializer
# #         return Response (data=response,status=status.HTTP_200_OK)
# #     elif request.method=="PUT":
# #         serializer=MovieSerializers(movie,data=request.data, partial=True)
# #         if serializer.is_valid(raise_exception=True):
# #             serializer.save()
# #             response["data"]=serializer
# #             return Response(data=response,status=status.HTTP_201_CREATED)
# #         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# #
#
#
#
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def movie_detail(request, slug):
#     try:
#         movie = Movie.objects.get(slug=slug)
#         response = {"success": True}
#     except Exception as e:
#         response["error"] = e
#         return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
#     # GET so'rov
#     if request.method == "GET":
#         serializer = MovieSerializers(movie)
#         return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
#
#     # PUT / PATCH so'rov
#     elif request.method in ["PUT", "PATCH"]:
#         partial = request.method == "PATCH"
#         serializer = MovieSerializers(movie, data=request.data, partial=partial)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#
#     # DELETE so'rov
#     elif request.method == "DELETE":
#         movie.delete()
#         return Response({"success": True, "message": "Movie deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['POST'])
# def ism_api(request):
#     ism = request.data['ism']
#     return Response(data={"ism": f"salom {ism}"})
