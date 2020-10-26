import unittest
from my_sum import sum_collection

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum_collection(data)
        self.assertEqual(result, 6)

    def test_list_float(self):
        data = [1.2, 2.4, 3.6, 4.8]
        result = sum_collection(data)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()