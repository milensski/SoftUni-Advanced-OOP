from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Seed, Meat]

    @property
    def gained_weight(self):
        return 0.35
