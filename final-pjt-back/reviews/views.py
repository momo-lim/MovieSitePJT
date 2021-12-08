from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from .models import Review, ReviewComment
from .serializers import ReviewCommentSerializer, ReviewListSerializer, ReviewCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import get_user_model
# Create your views here.


# Review 목록 출력
@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewCreateSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewCreateSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):   
            serializer.save()
            return Response(serializer.data)

    else:
        review.delete()
        data = {
            'delete':f'데이터 {review_pk}번이 삭제되었습니다.'
        }
    return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def review_comments(request, review_pk):
    comments = get_list_or_404(ReviewComment, review=review_pk)
    serializer = ReviewCommentSerializer(comments, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def review_comment_create(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     serializer = ReviewCommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(review=review, user=request.user)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','DELETE','PUT', 'POST'])
def review_comment_update(request, review_pk):
    # comment = get_object_or_404(ReviewComment, content=comment_content)
    
    # if request.method == 'PUT':
    #     serializer = ReviewComment(comment, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

    comments = ReviewComment.objects.all()
    comments.delete()

    for comment in request.data:
        user = get_object_or_404(get_user_model(), username=comment['user'])
        review = get_object_or_404(Review, pk=review_pk)
        new_comment = ReviewComment(user=user, review=review, content=comment['content'])
        new_comment.save()

    return Response(status=status.HTTP_204_NO_CONTENT)
        



