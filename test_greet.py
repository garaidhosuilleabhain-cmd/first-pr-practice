import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_strips_surrounding_whitespace(self):
        self.assertEqual(greet("  Ada  "), "Hello, Ada!")

    def test_empty_name_falls_back_to_world(self):
        self.assertEqual(greet(""), "Hello, world!")
        self.assertEqual(greet("   "), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
