import unittest

from farewell import farewell
from greet import greet


class GreetTests(unittest.TestCase):
    def test_greet_returns_formatted_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_farewell_returns_formatted_name(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")


if __name__ == "__main__":
    unittest.main()
