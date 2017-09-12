# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('slug', models.SlugField(max_length=256, verbose_name='\u7f51\u5740')),
                ('markdown_content', models.TextField()),
                ('html_content', models.TextField(editable=False)),
                ('status', models.IntegerField(default=1, choices=[(2, '\u5f85\u5ba1\u6279'), (4, '\u5b58\u6863'), (1, '\u8349\u7a3f'), (3, '\u5df2\u53d1\u5e03')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['modified'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=50, blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='cms.Category'),
        ),
    ]
