from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ArticleColumn
from .models import ArticlePost

admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)