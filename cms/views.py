# coding=utf-8
from cms.models import Article, Category
from django.shortcuts import render_to_response, get_object_or_404,render
from django.db.models import Q
from django.http.response import HttpResponse
import os
from django.template.loader import render_to_string
import sys
import logging


reload(sys)
sys.setdefaultencoding("utf8")

def home(request):  # catrgory list
    categories = Category.objects.all()
    return render_to_response("cms/index.html", {'categories': categories})


def category(request, slug):  # article list
    """Given a category slug,display all items in a category."""
    categories = Category.objects.all()
    cur_category = get_object_or_404(Category, slug=slug)
    article_list = Article.objects.filter(category=cur_category)
    heading = cur_category.label
    return render_to_response("cms/category.html", locals())  # 返回所有本地变量


def article(request, slug):  # article detail # 怎么设计的不同分类可重复？
    categories = Category.objects.all()
    cur_article = get_object_or_404(Article, slug=slug)
    # return render_to_response("cms/article.html", locals())  # 返回所有本地变量

    static_html = 'static_html/' + slug + '.html'

    logging.warning(os.path.abspath(static_html))

    if not os.path.exists(static_html):
        logging.warning("not exist")
        content = render_to_string('cms/article.html', locals())
        with open(static_html, 'w') as static_file:
            static_file.write(content)
    return render(request, static_html)


def search(request):
    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    categories = Category.objects.all()
    if 'q' in request.GET:
        term = request.GET('q')
        story_list = Article.objects.filter(Q(title__contains=term) | Q(markdown_content__contains=term))
        heading = "Search results"

    return render_to_response("cms/category.html", locals())


def test(requset, slug, slug2):
    cur_category = get_object_or_404(Category, slug=slug)
    cur_article = get_object_or_404(Article, category=cur_category, slug=slug2)
    return HttpResponse(cur_article.title)

