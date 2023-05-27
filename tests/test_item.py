"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from pytest import fixture

from src.item import Item

@fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_discount(item):
        item.apply_discount()
        assert item.price == 10000.0


def test_instantiate_from_csv(cls) -> None:
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5