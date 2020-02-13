import pytest

from articles.models.article import ArticleManager


def test_article_manager_find_article_by_uuid():
    articles = ArticleManager.get_articles(uuid='this-doesnt-exist-i-hope')

    assert len(articles) == 0

    articles = ArticleManager.get_articles(
        uuid='d6397ee8-c4da-11e7-a496-0050569d4be0'
    )

    assert len(articles) == 1


def test_article_manager_finds_first_article_by_slug():
    articles = ArticleManager.get_articles(slug='this-doesnt-exist-i-hope')

    assert len(articles) == 0

    articles = ArticleManager.get_articles(slug='10-promise')

    assert len(articles) == 1


def test_article_manager_loads_list_of_objects():

    articles = ArticleManager.get_articles()

    assert len(articles) > 0


def test_article_manager_exclude_uuid_filter():
    excluded_uuid = 'd6397ee8-c4da-11e7-a496-0050569d4be0'
    articles = ArticleManager.get_articles(
        exclude_uuid=excluded_uuid
    )
    assert len(articles) == 9
    for article in articles:
        assert article.uuid != excluded_uuid


def test_article_manager_raise_exception_if_invalid_content_api_path_given():

    with pytest.raises(Exception) as e_info:
        ArticleManager._get_articles_from_json(
            json_path="/tmp/thisDoesntExist.json")
        assert e_info.message == 'Article JSON file not found'
