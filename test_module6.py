import io
import sys
import unittest
from module6 import ItemToPurchase, ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Alice", "March 1, 2020")
        self.item1 = ItemToPurchase("A", 10, 1, "desc A")
        self.item2 = ItemToPurchase("B", 5, 2, "desc B")
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)

    def capture_print(self, fn, *args, **kwargs):
        buf = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buf
        try:
            fn(*args, **kwargs)
        finally:
            sys.stdout = old_stdout
        return buf.getvalue()

    def test_remove_nonexistent(self):
        out = self.capture_print(self.cart.remove_item, "X")
        self.assertIn("Item not found in cart. Nothing removed.", out)

    def test_modify_nonexistent(self):
        fake = ItemToPurchase("X", 1, 1, "x")
        out = self.capture_print(self.cart.modify_item, fake)
        self.assertIn("Item not found in cart. Nothing modified.", out)

    def test_get_counts_and_cost(self):
        self.assertEqual(self.cart.get_num_items_in_cart(), 3)
        self.assertEqual(self.cart.get_cost_of_cart(), 10*1 + 5*2)

    def test_print_total_empty(self):
        empty = ShoppingCart()
        out = self.capture_print(empty.print_total)
        self.assertIn("SHOPPING CART IS EMPTY", out)

    def test_print_descriptions(self):
        out = self.capture_print(self.cart.print_descriptions)
        self.assertIn("Item Descriptions", out)
        self.assertIn("A: desc A", out)

    def test_partial_modify(self):
        mod = ItemToPurchase("A", 20, 0, "none")
        self.cart.modify_item(mod)
        item = next(i for i in self.cart.cart_items if i.item_name == "A")
        self.assertEqual(item.item_price, 20)
        self.assertEqual(item.item_description, "desc A")

if __name__ == "__main__":
    unittest.main()
