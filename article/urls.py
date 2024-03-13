from django.urls import path
from . import views
app_name='artilce'

urlpatterns=[
    path('article-list/', views.article_list, name='article_list'),

    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 删除文章
    # path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article-safe-delete/<int:id>/',views.article_safe_delete,name='article_safe_delete'
    ),

    path('article-update/<int:id>/', views.article_update, name='article_update'),
]