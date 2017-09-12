# coding=utf-8
from cms.models import Article, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q


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
    return render_to_response("cms/article.html", locals())  # 返回所有本地变量


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

