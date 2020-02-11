import json

from articles.views import index, ArticleView


def test_index(rf):
    request = rf.get("/")
    response = index(request)

    assert 'This is the index' in str(response.content)


def test_article_view(rf):
    request = rf.get("/article")
    view = ArticleView()
    view.kwargs = {}
    response = view.get(request)
    content = json.loads(response.content)

    assert 'articles' in content
    assert len(content['articles']) > 0
    assert content['articles'][0] is not None
