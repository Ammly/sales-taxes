from unittest import TestCase
from main import display_receipt, total_item_cost, total_item_tax


class Test(TestCase):
    def test_display_receipt(self):
        """
            Test display receipt for 1 book at 12.49, not imported and not tax exempted
            basket = [(1, 'book', 12.49, False, True)]
        """
        basket = [(1, 'book', 12.49, False, True)]
        self.assertEqual(display_receipt(basket),
                         "\n1 book: 12.49 \nSales Taxes: 0.00 \nTotal: 12.49 \n")

    def test_total_item_cost(self):
        """
            Test Item cost for 1 book at 12.49, not imported and not tax exempted
            basket = [(1, 'book', 12.49, False, True)]
        """
        self.assertEqual(float(total_item_cost(12.49, 1, False, True)), 12.49)

    def test_total_item_tax(self):
        """
            Test total Tax for 1 book at 12.49, not imported and not tax exempted
            basket = [(1, 'book', 12.49, False, True)]
        """
        self.assertEqual(total_item_tax(12.49, False, True), 0.0)
