from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.reviews_list),
    path('create/', views.reviews_list),
    path('update/<int:review_pk>/', views.review_update_delete),
    path('detail/<int:review_pk>/', views.review_detail),
    path('detail/<int:review_pk>/comments/', views.review_comments),
    # path('detail/<int:review_pk>/createcomment/', views.review_comment_create),
    path('detail/<int:review_pk>/updatecomment/', views.review_comment_update),
]