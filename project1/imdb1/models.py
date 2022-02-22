from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    poster = models.ImageField()
    is_released = models.BooleanField(default=True)


class Cast(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='person')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film')
    film_char_name = models.CharField(max_length=30)




