import unittest
from programm import add, mult

class TestAddFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,5),7)
    def test_mult(self):
        self.assertEqual(mult(2,3),6)


if __name__ == "__main__":
    unittest.main()