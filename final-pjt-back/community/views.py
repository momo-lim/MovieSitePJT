from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Article,CommunityComment
from .serializers import ArticleListSerializer,CommunityCommentSerializer,ArticleSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def article_list(request):
    if request.method == 'GET':
        
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = ArticleListSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
@permission_classes([AllowAny])
def article_detail(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)

        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete':f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response('왜 안돼지')

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def article_comment_list(request,article_pk):
#     # comments = get_list_or_404(CommunityComment)
#     article = get_object_or_404(Article,pk=article_pk)
#     serializer = ArticleSerializer(article)
#     return Response(serializer.data)


@api_view(['DELETE','PUT'])
# @permission_classes([AllowAny])
def article_comment_detail(request,article_comment_pk):
    comment = get_object_or_404(CommunityComment,pk=article_comment_pk)

    # if request.method == 'GET':
    #     serializer = CommunityCommentSerializer(comment)
    #     return Response(serializer.data)
    
    if request.method == 'DELETE':
        comment.delete()
        data = {
            'message': f'댓글 {article_comment_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommunityCommentSerializer(comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def article_comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    serializer = CommunityCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article,user=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def article_likes(request,article_pk):
    print(request.user)
    # if request.user.is_authenticated:
    article = get_object_or_404(Article,pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        liked = False
    else:
        article.like_users.add(request.user)
        liked = True
    context = {
        'liked':liked,
        'count':article.like_users.count(),
    }
    return Response(context)
    # return Response('로그인 안됨')
    
        

