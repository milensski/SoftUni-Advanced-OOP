from unittest import TestCase,main


from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Dayzee', 'penguin', 'hugh')

    def test_initialize(self):

        self.assertEqual('Dayzee',self.mammal.name)
        self.assertEqual('penguin',self.mammal.type)
        self.assertEqual('hugh',self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)



if __name__ == '__main__':
    main()
