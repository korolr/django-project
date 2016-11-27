from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import *

def articles(request):
    posts = Article.objects.all().order_by('-article.article_date')
    return render_to_response('articles.html', {'articles': posts, })


def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id),})
