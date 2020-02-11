from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models.article import ArticleManager
from .serializers import serialize_article


def index(request):
    context = {}
    return render(request, 'index.html', context)


class ArticleView(View):
    def get(self, request):
        articles = ArticleManager.get_articles(
            slug=self.kwargs.get('slug')
        )
        return JsonResponse({
            "articles": [serialize_article(article) for article in articles]
        })
