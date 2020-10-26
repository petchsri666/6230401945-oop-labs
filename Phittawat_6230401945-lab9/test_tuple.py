import unittest
from my_sum import sum_collection


class TestSum(unittest.TestCase):
    def test_tuple_int(self):
        """
        Test that it can sum a list of integers
        """
        data = (1, 2, 3, 4)
        result = sum_collection(data)
        self.assertEqual(result, 10)

    def test_tuple_float(self):
        """
        Test that it can sum a list of integers
        """
        data = (1.2, 2.4, 3.6, 4.8)
        result = sum_collection(data)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()