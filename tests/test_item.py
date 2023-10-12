"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_calculate_total_price():
    item = Item('Смартфон', 1.0, 10)
    assert item.calculate_total_price() == 10.0


def test_apply_discount():
    item = Item('Смартфон', 1.0, 10)
    item.apply_discount()
    assert item.price == 0.85


def test_name():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_convert():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
