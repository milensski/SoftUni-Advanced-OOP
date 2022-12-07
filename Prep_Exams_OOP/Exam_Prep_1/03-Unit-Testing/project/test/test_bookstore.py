from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(15)
        self.books = {'C#': 2,
                      'Python': 3
                      }
        self.book = {"Python": 2}

    def test_init(self):
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_book_limit_setter(self):
        with self.assertRaises(ValueError) as v:
            self.store.books_limit = 0

        self.assertEqual('Books limit of 0 is not valid', str(v.exception))

    def test_book_counter(self):
        self.store.availability_in_store_by_book_titles = self.books
        self.assertEqual(5, len(self.store))

    def test_receive_limit_in_store_raise_exception(self):
        with self.assertRaises(Exception) as e:
            self.store.receive_book('Java', 20)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(e.exception))

    def test_receive_limit_in_store_with_enough_space_and_new_book(self):
        result = self.store.receive_book('Java', 5)
        self.assertEqual(self.store.availability_in_store_by_book_titles['Java'],5)
        self.assertEqual("5 copies of Java are available in the bookstore.",result)
        self.assertEqual({'Java': 5},self.store.availability_in_store_by_book_titles)

    def test_receive_limit_in_store_with_enough_space_and_existin_book(self):
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.receive_book('C#', 5)
        self.assertEqual(self.store.availability_in_store_by_book_titles['C#'],7)
        self.assertEqual("7 copies of C# are available in the bookstore.",result)

    def test_method_sell_book_raise_exception_if_book_not_exist_in_store(self):
        with self.assertRaises(Exception) as e:
            self.store.sell_book('Java', 3)
        self.assertEqual('Book Java doesn\'t exist!', str(e.exception))

    def test_method_sell_book_raise_exception_if_copies_not_enough(self):
        self.store.availability_in_store_by_book_titles = self.books
        with self.assertRaises(Exception) as e:
            self.store.sell_book('C#', 10)

        self.assertEqual("C# has not enough copies to sell. Left: 2", str(e.exception))

    def test_method_sell_book_successfully(self):
        self.store.availability_in_store_by_book_titles = self.books
        result = self.store.sell_book("C#",1)
        self.assertEqual(1,self.store.availability_in_store_by_book_titles['C#'])
        self.assertEqual("Sold 1 copies of C#",result)
        self.assertEqual(1,self.store._Bookstore__total_sold_books)

    def test_str_representation_method(self):
        self.store.availability_in_store_by_book_titles = self.book
        self.store._Bookstore__total_sold_books = 1
        result = str(self.store)
        expected = "Total sold books: 1\n" + "Current availability: 2\n" + " - Python: 2 copies"
        self.assertEqual(expected,result)

if __name__ == "__main__":
    main()
