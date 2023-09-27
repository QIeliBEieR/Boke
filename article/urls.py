from django.conf.urls.static import static
from django.urls import path

from article import views

app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 安全删除文章
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name='article_safe_delete'
    ),
    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]

# import django.conf
#
# if django.conf.settings.DEBUG:
#     urlpatterns += static(django.conf.settings.MEDIA_URL,
#                           document_root=django.conf.settings.MEDIA_ROOT)
