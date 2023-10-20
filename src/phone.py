from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return str(self.__name)

    @property
    def number_of_sim(self):
        return self.number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num_sim):
        if int(self.number_of_sim) != self.number_of_sim and self.number_of_sim > 0:
            self.__number_of_sim = num_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
