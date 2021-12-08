from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('profile/<str:username>/', views.profile),
    path('follow/<str:username>/', views.follow),
    path('genres/<str:username>/',views.genres)
]