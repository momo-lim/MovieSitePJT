from django.contrib import admin
from movies.models import Movie, MovieComment

# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieComment)