import unittest
from fundamentals import check_number
    
class TestNumber(unittest.TestCase):
    def test_check_number_odd_number(self):
        self.assertEqual(check_number(1,19))

    def test_check_number_even_range_2_to_5(self):
        self.assertEqual(check_number(2, 5))

    def test_check_number_even_range_6_to_20(self):
        self.assertEqual(check_number(6, 20))

    def test_check_number_even_range_6_to_20(self):
        self.assertEqual(check_number(6, 20))

    def test_check_number_negative_even_number(self):
        self.assertEqual(check_number(-2, -20))

    def test_check_number_negative_odd_number(self):
        self.assertEqual(check_number(-1, -19))

    def test_check_number_neutral(self):
        self.assertEqual(check_number(0))