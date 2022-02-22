from django.contrib import admin
from .models import Profile, Film, Cast


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'password', 'age', 'country']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'poster', 'is_released']


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'film', 'film_char_name']


