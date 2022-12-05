from horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    INCREASE_SPEED = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.INCREASE_SPEED > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.INCREASE_SPEED
