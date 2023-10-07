"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_calculate_total_price():
    item = Item('Смартфон', 1.0, 10)
    assert item.calculate_total_price() == 10.0

def test_apply_discount():
    item = Item('Смартфон', 1.0, 10)
    item.apply_discount()
    assert item.price == 0.85
