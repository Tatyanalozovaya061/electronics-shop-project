import os
import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл items_test.csv поврежден'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    discount = 0.85 # скидка 15%
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self.__name)

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]


    @classmethod
    def instantiate_from_csv(cls, csvfile='src/items.csv'):
        cls.all.clear()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.split(current_dir)[0]
        filepath = os.path.join(root_dir, csvfile)
        try:
            with open(filepath, 'r', encoding='windows-1251') as f:
                rows = csv.DictReader(f)
                for row in rows:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(name=name, price=price, quantity=quantity)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')

        except InstantiateCSVError:
            raise InstantiateCSVError('Файл items.csv поврежден')


    @staticmethod
    def string_to_number(num):
        return int(float(num))

    def calculate_total_price(self) -> str:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.discount
