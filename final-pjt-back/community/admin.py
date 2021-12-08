from django.contrib import admin

from community.models import Article, CommunityComment

# Register your models here.

admin.site.register(Article)
admin.site.register(CommunityComment)
