from project.animal import Animal

class Tiger(Animal):

    def __init__(self, name, age, gender):
        self.money_for_care = 45
        super().__init__(name,age,gender,self.money_for_care)