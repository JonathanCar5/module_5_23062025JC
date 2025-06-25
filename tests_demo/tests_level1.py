import unittest
from calculator2 import Calculator2

xy = Calculator2(a=6, b=7)
print(xy.get_product())

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator2(8,2)
        self.assetEqual(calculation.got_sum(), 10, 'The sum is wrong')

    def test_difference(self):
        calculation = Calculator2(10,6)
        self.assertEqual(Calculator2.get_difference(), 5)

    def test_get_product(self):
        calculation = Calculator2(8,2)
        self.assertEqual(Calculator2.get_product(), 50)

    def test_get_quotient(self):
        calculation = Calculator2(10,2)
        self.assertEqual(Calculator2.get_quotient(), 2.0)

    def test_divide_by_zero(self):
        calc_zero = Calculator2(a=10, b=0)
        with self.assertRaises(ValueError):
            calc_zero.get_quotient()

if __name__ == '__main__':
    unittest.main()