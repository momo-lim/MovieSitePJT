from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, UserDetailSerializer,UserGenreSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # Client가 보낸 데이터 중 비밀번호 확인
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 아이디 중복 확인
    username = request.data.get('username')
    if get_user_model().objects.all().filter(username=username).exists():
        return Response({'error': '아이디가 중복됩니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        # DB 반영
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)

    serializer = UserDetailSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, username):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), username=username)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                isFollowed = False
            else:
                you.followers.add(me)
                isFollowed = True
            context = {
                'isFollowed': isFollowed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)

@api_view(['GET'])
@permission_classes([AllowAny])
def genres(request,username):
    person = get_object_or_404(get_user_model(),username=username)
    serializer = UserGenreSerializer(person)
    return Response(serializer.data)