from .serializers import serialize_article
from .models.article import Article


def create_article(**kwargs):
    defaults = {
        "tags": [],
        "authors": [],
        "links": [],
        "recommendations": [],
        "disclosure": '',
        "promo": '',
        "body": '<b> great article </b>',
        "visibility": None,
        "article_type": 'great',
        "path": '/what-a-great-place/to-find-an-article',
        "uuid": 1,
        "author_override": None,
        "created": "",
        "headline": "Great!",
        "modified": None,
        "publish_at": None,
        "instruments": None,
        "static_page": '',
        "product_id": "abc",
        "bureau": '',
        "collection": '',
        "images": [],
        "video": '',
        "pitch": None,
        "byline": [],
    }
    defaults.update(**kwargs)

    return Article(**defaults)


def test_serialize_article_all_base_fields():
    my_great_article = create_article()
    serialized = serialize_article(my_great_article)

    assert 'tags' in serialized
    assert 'authors' in serialized
    assert 'headline' in serialized
    assert 'links' in serialized
    assert 'recommendations' in serialized


def test_pickling_of_complex_fields():
    tags = [{'uuid': '78aa4c44-d4f4-11e5-86ff-0050569d32b9', 'slug': 'msn', 'name': 'MSN', 'tag_type': {'name': 'Syndication Partner', 'slug': 'syndication-partner'}, 'links': {'content': 'http://api.fool.com/api/content?tag_uuids=78aa4c44-d4f4-11e5-86ff-0050569d32b9', 'self': 'http://api.fool.com/api/tags/78aa4c44-d4f4-11e5-86ff-0050569d32b9'}}, {'uuid': '342ec714-9adf-11e6-bdf0-0050569d32b9', 'slug': 'default-partners', 'name': 'Default Partners', 'tag_type': {'name': 'Syndication Partner', 'slug': 'syndication-partner'}, 'links': {'content': 'http://api.fool.com/api/content?tag_uuids=342ec714-9adf-11e6-bdf0-0050569d32b9', 'self': 'http://api.fool.com/api/tags/342ec714-9adf-11e6-bdf0-0050569d32b9'}},
            {'uuid': '89038dfe-5db3-11e3-8416-0050569d32b9', 'slug': '10-promise', 'name': '10% Promise', 'tag_type': {'name': 'Personalized Email', 'slug': 'personalized-email'}, 'links': {'content': 'http://api.fool.com/api/content?tag_uuids=89038dfe-5db3-11e3-8416-0050569d32b9', 'self': 'http://api.fool.com/api/tags/89038dfe-5db3-11e3-8416-0050569d32b9'}}, {'uuid': '603e544a-1f53-11e5-a69e-0050569d4be0', 'slug': 'yahoo-money', 'name': 'Yahoo', 'tag_type': {'name': 'Syndication Partner', 'slug': 'syndication-partner'}, 'links': {'content': 'http://api.fool.com/api/content?tag_uuids=603e544a-1f53-11e5-a69e-0050569d4be0', 'self': 'http://api.fool.com/api/tags/603e544a-1f53-11e5-a69e-0050569d4be0'}}]

    my_great_article = create_article(tags=tags)
    serialized = serialize_article(my_great_article)

    assert 'tags' in serialized

    assert serialized['tags'] == tags
