class Hero:

    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self):
        return f'{self.username} of type ' \
               f'{self.__class__.__name__} has ' \
               f'level {self.level} '

