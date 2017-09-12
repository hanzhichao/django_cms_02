# coding=utf-8
from __future__ import unicode_literals

from django.db import models
import datetime
from django.db.models import permalink
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from markdown import markdown
from django.contrib import admin

VIEWABLE_STATUS = [3, 4]


# @python_2_unicode_compatible  # 向后兼容django版本
class Category(models.Model):
    """文章分类"""
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = '分类'

    @permalink
    def get_absolute_url(self):  # 获取reverse后的链接
        # return ('cms-article', (), {'slug': self.slug})
        return 'cms-category', (), {'slug': self.slug}  # 尝试一下是否可以

    def __unicode__(self):
        return self.label


# @python_2_unicode_compatible  # 向后兼容django版本，可以使用 def __str__()
class Article(models.Model):
    """ 文章页面 """

    STATUS_CHOICES = {
        (1, '草稿'),
        (2, '待审批'),
        (3, '已发布'),
        (4, '存档')
    }

    title = models.CharField('标题', max_length=256)
    slug = models.SlugField('网址', max_length=256, db_index=True)  # 建立数据库索引
    category = models.ForeignKey(Category)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)  # invisible
    # author = models.ForeignKey(User, blank=True, null=True)
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=1)
    # created = models.DateTimeField(default=datetime.datetime.now)  # 可以杜撰
    created = models.DateTimeField('创建时间', auto_now_add=True)  # 第一次创建更改
    # modified = models.DateTimeField(default=datetime.datetime.now) # 可以杜撰
    modified = models.DateTimeField('最后修改时间', auto_now=True)  # 每次保存时间

    class Meta:
        ordering = ['modified']
        verbose_name = '文章'  # 单数 中文下显示
        verbose_name_plural = '文章'  # 复数，中文下显示

    @permalink
    def get_absolute_url(self):  # 获取reverse后的链接
        # return ('cms-article', (), {'slug': self.slug})
        return 'cms-article', (), {'slug': self.slug}  # 尝试一下是否可以

    # def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
    #     return self.title

    def save(self, *args, **kws):  # 转换markdown内容为html内容
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Article, self).save()


class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager, self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)
