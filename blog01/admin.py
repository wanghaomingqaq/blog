from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog01.models import Article,User,Category,Tag,ArticleComment
from . import models
# Register your models here.
#ass ArticleAdmin(admin.ModelAdmin):

class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'body', 'title']
    search_fields = ['title']  # 搜索框

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(ArticleComment,CommentAdmin)
