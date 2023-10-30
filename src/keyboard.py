from src.item import Item


class MixinLanguage:
    def __init__(self, name: str, price: float, quantity: int, language) -> None:
        self.__language = language
        super().__init__(name, price, quantity)

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLanguage, Item):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity, language)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.__language})"
