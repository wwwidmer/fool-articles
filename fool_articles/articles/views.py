from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models.article import ArticleManager
from .serializers import serialize_article


def index(request):
    headliners = ArticleManager.get_articles(slug="10-promise")

    context = {
        "headline_article": headliners[0],
        "articles": ArticleManager.get_articles()[:3]
    }
    return render(request, 'index.html', context)


class ArticleView(View):
    def get(self, request, **kwargs):
        articles = ArticleManager.get_articles(
            slug=self.kwargs.get('slug'),
            uuid=self.kwargs.get('uuid')
        )
        context = {
            "articles": [
                serialize_article(article) for article in articles
            ]
        }

        if request.META.get('HTTP_ACCEPT') == 'application/json':
            return JsonResponse(context)

        return render(request, 'article.html', context)
