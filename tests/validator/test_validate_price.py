from app.validator import validate_price
import pytest
from jsonschema.exceptions import ValidationError


ok_prices = [
    {"value": 1050, "currency": "USD"},
    {"value": 0, "currency": "EUR"},
]

ko_prices = [
    {"value": 1050, "currency": "wrong currency"},
    {"value": "wrong value", "currency": "USD"},
    {"value": 10.50, "currency": "USD"},
    {"value": -1, "currency": "EUR"},
    {"value": 1050, "currency": "USD", "wrong_key": "whatever"},
    {"value": 1050},
    {"currency": "USD"},
    {},
]


@pytest.mark.parametrize("price", ok_prices)
def test_ok(price):
    validate_price(price)


@pytest.mark.parametrize("price", ko_prices)
def test_ko(price):
    with pytest.raises(ValidationError):
        validate_price(price)
