from abc import ABC, abstractmethod


class Delicacy(ABC):

    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion #in grams
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace() or len(value) == 0:
            raise ValueError("Name cannot be null or whitespace!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):

        if value <= 0.0:
            raise ValueError("Price cannot be less or equal to zero!")

        self.__price = value

    @abstractmethod
    def details(self):
        pass

