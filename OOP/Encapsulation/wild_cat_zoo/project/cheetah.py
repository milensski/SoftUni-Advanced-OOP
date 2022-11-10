from project.animal import Animal

class Cheetah(Animal):

    def __init__(self, name, age, gender):
        self.money_for_care = 60
        super().__init__(name,age,gender,self.money_for_care)