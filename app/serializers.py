from rest_framework import serializers

from .models import *

# class MovieSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields='__all__'




from enum import unique

from rest_framework import serializers
from app.models import *


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(required=False)
    title = serializers.CharField(max_length=150)
    year = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(many=True,queryset=Actors.objects.all())

    def create(self, validated_data):
        actors_data = validated_data.pop('actors', [])  # ManyToManyField ajratish
        movie = Movie.objects.create(**validated_data)  # Movie yaratish
        movie.actors.set(actors_data)  # ManyToManyField bog'lash
        return movie
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.slug = validated_data.get('slug',instance.slug)
        instance.year = validated_data.get('year',instance.year)
        instance.genre = validated_data.get('genre',instance.genre)
        if 'actors' in validated_data:
            instance.actors.set(validated_data['actors'])
        instance.save()
        return instance


class ActorsSerializer(serializers.Serializer):
    id  = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    slug = serializers.SlugField(required=False)

    def create(self, validated_data):
        return Actors.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.birth_date = validated_data.get('birth_date',instance.birth_date)
        instance.save()
        return instance
