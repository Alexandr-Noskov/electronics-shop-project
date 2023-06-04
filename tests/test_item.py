"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from pytest import fixture

from src.item import Item

from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)

@pytest.fixture()
def make_phone():
    return Phone("iPhone 14", 120000, 5, 2)

def test_init(item):
    assert item.quantity == 20

def test_calculate_total_price(item):
    assert Item.calculate_total_price() == 200000

def test_apply_discount(item):
        Item.apply_discount()
        assert Item.price == 10000.0


def test_instantiate_from_csv(cls) -> None:
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5


def test_name_too_long_len(item):
    """Название товара слишком длинное"""
    with pytest.raises(Exception):
        item.name = 'ТелефонТелефонТелефон'

def test__repr__():
    assert repr(item) == "Item('Смартфон', 10000, 20)"

def test__str__(item1=None):
    assert str(item1) == 'Смартфон'

def test_addition(make_item, make_phone):
    item1 = make_item
    phone1 = make_phone
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        assert item1 + 10 == 40
        assert phone1 + 5 == 20