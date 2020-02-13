import json

from articles.views import index, ArticleView


def test_index(client):
    response = client.get("/")

    assert 'main-article' in str(response.content)

    assert response.context['headline_article'] is not None
    assert len(response.context['articles']) == 3
    # TODO How to test the randomness


def test_article_view(rf):
    request = rf.get("/article", HTTP_ACCEPT='application/json')

    view = ArticleView()
    view.kwargs = {}
    response = view.get(request, HTTP_ACCEPT='application/json')
    content = json.loads(response.content)

    assert 'articles' in content
    assert len(content['articles']) > 0
    assert content['articles'][0] is not None


def test_article_view_slug(rf):
    request = rf.get("/article/10-promise", HTTP_ACCEPT='application/json')

    view = ArticleView()
    view.kwargs = {
        'slug': '10-promise'
    }
    response = view.get(request)
    content = json.loads(response.content)

    assert 'articles' in content
    assert len(content['articles']) == 1
    assert content['articles'][0] is not None


def test_article_view_uuid(rf):
    request = rf.get("/article/10-promise", HTTP_ACCEPT='application/json')
    view = ArticleView()
    view.kwargs = {
        'uuid': 'd6397ee8-c4da-11e7-a496-0050569d4be0'
    }
    response = view.get(request)

    content = json.loads(response.content)

    assert 'articles' in content
    assert len(content['articles']) == 1
    assert content['articles'][0] is not None


def test_article_return_template(rf):
    request = rf.get("/article/10-promise")
    view = ArticleView()
    view.kwargs = {
        'slug': '10-promise'
    }
    response = view.get(request)

    assert response._headers['content-type'] == (
        'Content-Type', 'text/html; charset=utf-8'
    )
    assert '<!DOCTYPE html>' in str(response.content)
