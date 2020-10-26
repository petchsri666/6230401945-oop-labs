import unittest
import math_test


class TestMath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(math_test.sum(1,2),3)
        self.assertEqual(math_test.sum(1.1, 2.3), 3.4)

    def test_subtract(self):
        self.assertEqual(math_test.subtract(10, 2), 8)
        self.assertEqual(math_test.subtract(-3, 2), -5)

    def test_mul(self):
        self.assertEqual(math_test.mul(2, 3), 6)
        self.assertEqual(math_test.mul(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(math_test.divine(10, 2), 5)
        self.assertEqual(math_test.divine(3, 2), 1.5)
        self.assertRaises(ValueError, math_test.divine, 12, 0)


if __name__ == '__main__':
    unittest.main()
