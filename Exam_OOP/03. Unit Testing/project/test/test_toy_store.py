from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_initialization(self):
        shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(shelf, self.store.toy_shelf)

    def test_add_not_existing_shelf_exception(self):
        with self.assertRaises(Exception) as e:
            self.store.add_toy('H', 'abc')

        self.assertEqual("Shelf doesn't exist!", str(e.exception))

    def test_add_toy_already_existing_exception(self):
        self.store.toy_shelf['A'] = 'abc'
        with self.assertRaises(Exception) as e:
            self.store.add_toy('A', 'abc')
        self.assertEqual("Toy is already in shelf!", str(e.exception))

    def test_add_toy_to_not_none_shelf_exception(self):
        self.store.toy_shelf['A'] = 'abc'
        with self.assertRaises(Exception) as e:
            self.store.add_toy('A', 'dfg')
        self.assertEqual("Shelf is already taken!", str(e.exception))

    def test_add_toy_success(self):
        result = self.store.add_toy('A', 'abc')
        expect = "Toy:abc placed successfully!"
        self.assertEqual(result, expect)
        self.assertEqual('abc', self.store.toy_shelf['A'])

    def test_remove_toy_from_not_existing_shelf_exception(self):
        with self.assertRaises(Exception) as e:
            self.store.remove_toy('H', 'abc')

        self.assertEqual("Shelf doesn't exist!", str(e.exception))

    def test_remove_toy_not_existing_exception(self):
        self.store.toy_shelf['A'] = 'abc'
        with self.assertRaises(Exception) as e:
            self.store.remove_toy('A', 'abv')

        self.assertEqual("Toy in that shelf doesn't exists!", str(e.exception))

    def test_remove_toy_success(self):
        shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.store.toy_shelf['A'] = 'abc'
        result = self.store.remove_toy('A', 'abc')
        expect = "Remove toy:abc successfully!"
        self.assertEqual(result, expect)
        self.assertEqual(shelf, self.store.toy_shelf)


if __name__ == "__main__":
    main()
