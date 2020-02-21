from typing import List

import os
import json
from jsonschema import validate


SCHEMA_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)
), "quotes_json_schema.json")


class StockQuote:
    def __init__(self,
                 InstrumentId,
                 CompanyName="", Symbol="", Exchange="NYSE",
                 Description="", PercentChange=0,
                 Change=0, CurrentPrice=0,
                 ** kwargs
                 ):
        self.company_name = CompanyName
        self.symbol = Symbol
        self.exchange = Exchange
        self.change = Change
        self.current_price = CurrentPrice
        self.percent_change = PercentChange
        self.instrument_id = InstrumentId


class StockQuoteManager:

    @classmethod
    def get_quotes(cls, instrument_id=None) -> List[StockQuote]:

        results = [StockQuote(**quote)
                   for quote in cls._get_quotes_from_json()]
        if instrument_id is not None:
            def filter_func(
                stock_quote
            ):
                return stock_quote.instrument_id == instrument_id

            filtered_results = filter(filter_func, results)
            return list(filtered_results)

        return results

    @classmethod
    def _get_quotes_from_json(
        cls, json_path='content-api/quotes_api.json'
    ):
        '''
        Extremely similar to the json reader in articles.models.ArticleManager

        Consider DRYing this out
        '''
        if not os.path.exists(json_path):
            raise Exception("Article JSON file not found")

        with open(json_path) as content_raw_json:
            content_json = json.loads(content_raw_json.read())

        with open(SCHEMA_PATH) as schema_json:
            schema = json.loads(schema_json.read())

        validate(instance=content_json, schema=schema)
        return content_json
