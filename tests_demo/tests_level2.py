import unittest
from calculator2 import Calculator2

class TestOperatopms(unittest.TestCase):

    def setup(self):
        self.calculation = Calculator2(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.got_sum(), 10, 'The sum is wrong')

    def test_difference(self):
        self.assertEqual(self.calculation.get_difference(), 6, 'The difference is wrong')

    def test_get_product(self):
        self.assertEqual(self.calculation.get_product(), 16, 'The product is wrong')

    def test_get_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4.0, 'The quotient is wrong')

    def test_divide_by_zero(self):
        calc_zero = Calculator2(a=10, b=0)
        with self.assertRaises(ValueError):
            calc_zero.get_quotient()

if __name__ == '__main__':
    unittest.main()