import unittest
from practice1 import add, multiply, power


class TestPractice1Functions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add(10, 30), 40)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 6), 30)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 5), 0)

    def test_power(self):
        self.assertEqual(power(3, 3), 27)
        self.assertEqual(power(10, 0), 1)
        self.assertEqual(power(5, 3), 125)
       # self.assertEqual(power(5, 1), 125)


if __name__ == '__main__':
    unittest.main()
