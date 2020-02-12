
from stock_quotes.models import StockQuoteManager


def test_get_stock_quotes():
    quotes = StockQuoteManager.get_quotes()

    assert len(quotes) > 0
