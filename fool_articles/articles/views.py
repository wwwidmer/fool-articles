from random import sample

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView

from stock_quotes.models import StockQuoteManager
from stock_quotes.serializers import serialize_quote

from .models.comment import Comment
from .models.article import ArticleManager
from .serializers import serialize_article


def index(request):
    headliners = ArticleManager.get_articles(slug="10-promise")

    random_articles = []
    if len(headliners):
        articles = ArticleManager.get_articles(
            exclude_uuid=headliners[0].uuid
        )
        random_articles = sample(articles, 3)

    context = {
        "headline_article": headliners[0]
        if len(headliners) else None,
        "articles": random_articles
    }
    return render(request, 'index.html', context)


class ArticleView(View):
    def get(self, request, **kwargs):
        articles = ArticleManager.get_articles(
            slug=self.kwargs.get('slug'),
            uuid=self.kwargs.get('uuid')
        )
        quotes = StockQuoteManager.get_quotes()[:3]

        context = {
            "articles": [
                serialize_article(article) for article in articles
            ],
            "stock_quotes": [
                serialize_quote(quote) for quote in quotes
            ]
        }

        if request.META.get('HTTP_ACCEPT') == 'application/json':
            return JsonResponse(context)

        return render(request, 'article.html', context)


class CommentView(View):
    pass


class CommentListView(ListView):
    model = Comment

    def get_queryset(self):
        comments = Comment.objects.filter(article_uuid=self.kwargs['uuid'])
        return comments

    def render_to_response(self, context, **response_kwargs):
        data = {
            "comment_list": [],
            "page_obj": None,
            "is_paginated": False,

        }
        return JsonResponse(
            data,
            **response_kwargs

        )
