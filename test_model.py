# test_model.py
import unittest
from model import CalculatorModel

class TestCalculatorModel(unittest.TestCase):

    def setUp(self):
        self.model = CalculatorModel()

    def test_add(self):
        self.assertEqual(self.model.operate(3, 5, '+'), 8)

    def test_subtract(self):
        self.assertEqual(self.model.operate(10, 4, '−'), 6)

    def test_multiply(self):
        self.assertEqual(self.model.operate(7, 6, '×'), 42)

    def test_divide(self):
        self.assertEqual(self.model.operate(20, 5, '÷'), 4)

    def test_divide_by_zero(self):
        self.assertEqual(self.model.operate(5, 0, '÷'), 'Error')

    def test_reciprocal(self):
        self.assertEqual(self.model.reciprocal(4), 0.25)

    def test_reciprocal_zero(self):
        self.assertEqual(self.model.reciprocal(0), 'Error')

    def test_square(self):
        self.assertEqual(self.model.square(3), 9)

    def test_sqrt(self):
        self.assertEqual(self.model.sqrt(9), 3)
        self.assertAlmostEqual(self.model.sqrt(2), 2 ** 0.5)

    def test_sqrt_negative(self):
        self.assertEqual(self.model.sqrt(-4), 'Error')

    def test_percent(self):
        self.assertEqual(self.model.percent(80), 0.8)

    def test_plus_minus(self):
        self.assertEqual(self.model.plus_minus(7), -7)
        self.assertEqual(self.model.plus_minus(-5), 5)

if __name__ == '__main__':
    unittest.main()
