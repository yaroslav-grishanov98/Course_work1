from datetime import datetime

import pytest

from src.views import generate_events_page_response, generate_main_page_response


@pytest.fixture
def setup_test_data():
    return "data/operations.xlsx"


def test_main_page_response(setup_test_data):
    """Тест генерации ответа для главной страницы."""
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = generate_main_page_response(date_str)

    assert "greeting" in response
    assert "cards" in response
    assert "top_transactions" in response
    assert "currency_rates" in response
    assert "stock_prices" in response

    assert isinstance(response["greeting"], str)
    assert isinstance(response["cards"], list)
    assert isinstance(response["top_transactions"], list)
    assert isinstance(response["currency_rates"], list)
    assert isinstance(response["stock_prices"], list)

    assert response["greeting"] in [
        "Доброе утро",
        "Добрый день",
        "Добрый вечер",
        "Доброй ночи",
    ]


def test_events_page_response(setup_test_data):
    """Тест генерации ответа для страницы событий."""
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for period in ["W", "M", "Y", "ALL"]:
        response = generate_events_page_response(date_str, period)

        assert "expenses" in response
        assert "income" in response
        assert "currency_rates" in response
        assert "stock_prices" in response

        expenses = response["expenses"]
        assert "total_amount" in expenses
        assert "main" in expenses
        assert "transfers_and_cash" in expenses
        assert isinstance(expenses["main"], list)
        assert isinstance(expenses["transfers_and_cash"], list)

        income = response["income"]
        assert "total_amount" in income
        assert "main" in income
        assert isinstance(income["main"], list)
