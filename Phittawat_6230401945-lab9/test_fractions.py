import unittest
from my_sum import sum_collection
from fractions import Fraction


class TestFractions(unittest.TestCase):
    def test_list_fraction(self):
        """
        Test that it can sum a list of integers
        """
        data = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]
        result = sum_collection(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()