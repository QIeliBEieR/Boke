from django.contrib import admin

# Register your models here.

# 导入已经定义的ArticlePost模型
from .models import ArticlePost


# 注册ArticlePostAdmin

class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'body', 'created', 'updated', ]


#
admin.site.register(ArticlePost, ArticlePostAdmin)
admin.site.site_tittle = "my_blog（后台）"  # 登录界面
admin.site.site_header = "my_blog（后台）"  # 登录成功后的界面
