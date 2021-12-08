from rest_framework import serializers
from .models import Article,CommunityComment
from accounts.serializers import UserDetailSerializer
from rest_framework.fields import CurrentUserDefault


class ArticleListSerializer(serializers.ModelSerializer):
    # user = CurrentUserDefault()
    created_at = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    user = serializers.StringRelatedField()
    # username = serializers.SerializerMethodField()
    class Meta:
        model = Article
        
        fields = '__all__'
        read_only_fields=('user','like_users','category',)
       
class CommunityCommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    
    class Meta:
        model = CommunityComment
        fields = '__all__'
        read_only_fields=('article',)

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    communitycomment_set = CommunityCommentSerializer(many=True,read_only=True)
    # community_comment_count = serializers.IntegerField(source='communitycomment_set.count',read_only=True)
    class Meta:
        model = Article
        fields='__all__'
        read_only_fields=('user','like_users','category','created_at')