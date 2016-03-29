from django.contrib import admin

# Register your models here.
from django.contrib import admin
from article.models import Article, Comments
from django.contrib.auth import get_user_model
User = get_user_model()

class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']


admin.site.register(Article, ArticleAdmin)
