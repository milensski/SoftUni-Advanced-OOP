from project.animal import Animal

class Lion(Animal):

    def __init__(self, name, age, gender):
        self.money_for_care = 50
        super().__init__(name,age,gender,self.money_for_care)



