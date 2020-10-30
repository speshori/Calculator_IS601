import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, calculator)

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_square(self):
        self.assertEqual(self.calc.square(4), 16)

if __name__ == '__main__':
    unittest.main()
