from django.urls import path
from . import views

urlpatterns = [
    path('articles/',views.article_list),
    path('articles/<int:article_pk>/',views.article_detail),
    # path('article_comments/<int:article_pk>/',views.article_comment_list),
    path('articles/<int:article_pk>/comments/',views.article_comment_create),
    path('article/comment/<int:article_comment_pk>/',views.article_comment_detail),
    path('articles/<int:article_pk>/likes/',views.article_likes),
]
