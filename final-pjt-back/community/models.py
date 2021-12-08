from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

    def __str__(self):
        return self.title
    

class CommunityComment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    