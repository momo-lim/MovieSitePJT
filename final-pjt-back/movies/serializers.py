from rest_framework import serializers
from .models import Movie
from reviews.serializers import ReviewListSerializer

class MovieSerializer(serializers.ModelSerializer):

    review_set = ReviewListSerializer(many=True,read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'