class Player:

    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        info = []
        info.append(f'Player: {self.__name}')
        info.append(f'Sprint: {self.__sprint}')
        info.append(f'Dribble: {self.__dribble}')
        info.append(f'Passing: {self.__passing}')
        info.append(f'Shooting: {self.__shooting}')
        return '\n'.join(info)