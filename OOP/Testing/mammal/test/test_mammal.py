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

    def test_makesound(self):
        result = self.mammal.make_sound()
        expected = "Dayzee makes hugh"

        self.assertEqual(expected, result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected = 'animals'
        self.assertEqual(expected, result)


    def test_info_function(self):
        result = self.mammal.info()
        expected = "Dayzee is of type penguin"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()