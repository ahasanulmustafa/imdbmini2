from rest_framework import serializers
from .models import Profile, Film, Cast


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'email', 'password', 'age', 'country')


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'release_date', 'poster', 'is_released')


class CastSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    film = FilmSerializer(read_only=True)

    class Meta:
        model = Cast
        fields = ('id', 'profile', 'film', 'film_char_name')




