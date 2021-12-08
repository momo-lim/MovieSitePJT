from rest_framework import serializers
from .models import Review, ReviewComment

class ReviewListSerializer(serializers.ModelSerializer):
    # 영화 이름 출력
    movie = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    # 날짜 포맷 변경

    # 현재 시간을 구하고, 현재 시간과 created_at이 같은 날짜면 포맷을 '시간:분'으로 serialize
    # 그게 아니라면, '년-월-일'로 serialize 
    # current = datetime.datetime.now()

    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('movie', 'title', 'user', 'created_at', 'views')

class ReviewCommentSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()

    class Meta:
        model = ReviewComment
        fields = ('content', 'user')

class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields=('user',)