from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from community.models import Article
from reviews.serializers import ReviewListSerializer



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'genres')

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields='__all__'
    


class UserDetailSerializer(serializers.ModelSerializer):
    
    # 장르 id가 아니라 장르의 '__str__'클래스 값을 표현하는 StringRelatdField를 사용한다
    genres= serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)
    like_movies = MovieSerializer(read_only=True, many=True)
    post_articles = ArticleSerializer(read_only=True, many=True)
    post_reviews = ReviewListSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'genres', 'is_expert', 'followings', 'like_movies', 'post_articles', 'followers', 'post_reviews')


class UserGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('genres',)