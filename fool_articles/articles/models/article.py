from typing import List

import os
import json
from jsonschema import validate

SCHEMA_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)
), "content_api_json_schema.json")


class Article:
    def __init__(self,
                 disclosure, promo, body, visibility,
                 article_type, publish_at, path,
                 static_page, author_override,
                 uuid, created, headline, modified, product_id, instruments,
                 authors, bureau, collection,
                 tags, recommendations, images,
                 video, pitch, links,
                 byline
                 ):
        pass


class ArticleManager:

    @classmethod
    def get_articles(cls, slug=None) -> List[Article]:
        results = cls.get_articles_page_from_json()['results']
        if not slug:
            return results

        return list(
            filter(lambda article: article['tags'] == slug, results)
        )

    @classmethod
    def get_articles_page_from_json(
            cls, json_path='content-api/content_api.json'
    ):
        if not os.path.exists(json_path):
            raise Exception("Article JSON file not found")

        with open(json_path) as content_raw_json:
            content_json = json.loads(content_raw_json.read())

        with open(SCHEMA_PATH) as schema_json:
            schema = json.loads(schema_json.read())

        validate(instance=content_json, schema=schema)
        return content_json
