from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.enums import Choices
from movies.models import Genre

# Create your models here.

class User(AbstractUser):

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    is_expert = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.username
    