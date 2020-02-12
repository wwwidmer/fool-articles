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
        self.disclosure = disclosure
        self.promo = promo
        self.body = body
        self.visibility = visibility
        self.article_type = article_type
        self.publish_at = publish_at
        self.path = path
        self.static_page = static_page
        self.author_override = author_override
        self.uuid = uuid
        self.created = created
        self.headline = headline
        self.product_id = product_id
        self.instruments = instruments
        self.authors = authors
        self.bureau = bureau
        self.collection = collection
        self.tags = tags
        self.recommendations = recommendations
        self.images = images
        self.video = video
        self.pitch = pitch
        self.links = links
        self.byline = byline


class ArticleManager:

    @classmethod
    def get_articles(cls, slug=None, uuid=None) -> List[Article]:
        # Requirement:
        # Get the first article whose tag matches the param
        results = [
            Article(**result)
            for result in cls._get_articles_page_from_json()['results']
        ]
        if slug or uuid:
            assert not (
                slug and uuid
            ), 'Finding by both slug and uuid is not supported'
            if slug:
                def filter_func(result): return slug in [
                    tag['slug'] for tag in result.tags]
            if uuid:
                def filter_func(result): return result.uuid == uuid
            filtered_results = filter(filter_func, results)
            try:
                return [next(filtered_results)]
            except StopIteration:
                return []

        return results

    @classmethod
    def _get_articles_page_from_json(
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
