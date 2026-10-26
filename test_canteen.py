import unittest

from canteen import calculate_total


class TestCalculateTotal(unittest.TestCase):

    def test_amount_below_300(self):
        self.assertEqual(calculate_total(100), 105.00)

    def test_amount_equal_to_300(self):
        self.assertEqual(calculate_total(300), 315.00)

    def test_amount_above_300(self):
        self.assertEqual(calculate_total(400), 378.00)

    def test_amount_with_decimal(self):
        self.assertAlmostEqual(calculate_total(350.50), 331.22, places=2)
        
    def test_zero_subtotal(self):
        self.assertEqual(calculate_total(0), 0.00)

    def test_negative_subtotal(self):
        with self.assertRaises(ValueError):
            calculate_total(-100)


if __name__ == "__main__":
    unittest.main()