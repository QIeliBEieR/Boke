from django.db import models

# Create your models here.

# 导入内建的User模型
from django.contrib.auth.models import User
# 导入timezone用于时间处理的业务
from django.utils import timezone


# 博客文章的数据模型
class ArticlePost(models.Model):
    # 文章作者；on_delete参数用于指定删除数据的方式（级联）,关联User类（一对多）
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题；用字符串保存即可
    title = models.CharField(max_length=100)

    # 文章正文；大文本
    body = models.TextField()

    # 文章创建时间；参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间; 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 文章浏览量：
    total_views = models.PositiveIntegerField(default=0)


    class Meta:
        # ordering 按照创建时间倒序
        ordering = ('-created', )

    def __str__(self):
        # 返回文章标题
        return self.title



