import unittest

from lib.main import divide


class TestMain(unittest.TestCase):
    def test_divide_int(self):
        self.assertEqual(divide(2, 1), 2)

    def test_divide_float(self):
        self.assertEqual(divide(3, 2), 1.5)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
