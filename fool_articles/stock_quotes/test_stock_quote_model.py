
from stock_quotes.models import StockQuoteManager


def test_get_stock_quotes():
    quotes = StockQuoteManager.get_quotes()

    assert len(quotes) > 0


def test_get_stock_quote_by_instrument_id_unhappy_path():

    quotes = StockQuoteManager.get_quotes(
        instrument_id=9999999999999999999999999
    )

    assert len(quotes) == 0


def test_get_stock_quote_by_instrument_id_happy_path():

    quotes = StockQuoteManager.get_quotes(
        instrument_id=203781
    )

    assert len(quotes) == 1
