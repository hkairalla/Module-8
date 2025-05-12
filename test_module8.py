import io
import sys
import unittest
from unittest.mock import patch
from module8 import ItemToPurchase, ShoppingCart, print_menu, main

class TestItemToPurchase(unittest.TestCase):
    """Test the ItemToPurchase class functionality"""
    
    def test_default_constructor(self):
        """Test that default constructor initializes with correct default values"""
        item = ItemToPurchase()
        self.assertEqual(item.item_name, "none")
        self.assertEqual(item.item_price, 0)
        self.assertEqual(item.item_quantity, 0)
        self.assertEqual(item.item_description, "none")
    
    def test_parameterized_constructor(self):
        """Test that parameterized constructor sets values correctly"""
        item = ItemToPurchase("Test Item", 9.99, 3, "Test Description")
        self.assertEqual(item.item_name, "Test Item")
        self.assertEqual(item.item_price, 9.99)
        self.assertEqual(item.item_quantity, 3)
        self.assertEqual(item.item_description, "Test Description")
    
    def test_print_item_cost(self):
        """Test that print_item_cost outputs the correct format"""
        item = ItemToPurchase("Bottled Water", 1, 10, "Refreshing water")
        
        # Capture stdout to check output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        item.print_item_cost()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "Bottled Water 10 @ $1 = $10")


class TestShoppingCart(unittest.TestCase):
    """Test the ShoppingCart class functionality"""
    
    def setUp(self):
        """Set up test fixtures before each test"""
        self.cart = ShoppingCart("John Doe", "May 11, 2025")
        self.item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Volt color, Weightlifting shoes")
        self.item2 = ItemToPurchase("Chocolate Chips", 3, 5, "Semi-sweet")
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
    
    def capture_output(self, function, *args, **kwargs):
        """Helper method to capture printed output from functions"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        function(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()
    
    def test_default_constructor(self):
        """Test default constructor initializes with correct default values"""
        empty_cart = ShoppingCart()
        self.assertEqual(empty_cart.customer_name, "none")
        self.assertEqual(empty_cart.current_date, "January 1, 2020")
        self.assertEqual(len(empty_cart.cart_items), 0)
    
    def test_parameterized_constructor(self):
        """Test parameterized constructor sets values correctly"""
        self.assertEqual(self.cart.customer_name, "John Doe")
        self.assertEqual(self.cart.current_date, "May 11, 2025")
        self.assertEqual(len(self.cart.cart_items), 2)
    
    def test_add_item(self):
        """Test adding an item to the cart"""
        new_item = ItemToPurchase("Powerbeats", 128, 1, "Bluetooth headphones")
        initial_count = len(self.cart.cart_items)
        self.cart.add_item(new_item)
        self.assertEqual(len(self.cart.cart_items), initial_count + 1)
        self.assertEqual(self.cart.cart_items[-1].item_name, "Powerbeats")
    
    def test_remove_item_found(self):
        """Test removing an existing item from the cart"""
        initial_count = len(self.cart.cart_items)
        self.cart.remove_item("Nike Romaleos")
        self.assertEqual(len(self.cart.cart_items), initial_count - 1)
        names = [item.item_name for item in self.cart.cart_items]
        self.assertNotIn("Nike Romaleos", names)
    
    def test_remove_item_not_found(self):
        """Test that proper message is displayed when removing non-existent item"""
        output = self.capture_output(self.cart.remove_item, "NonExistentItem")
        self.assertIn("Item not found in cart. Nothing removed.", output)
    
    def test_modify_item_found(self):
        """Test modifying an existing item in the cart"""
        modified_item = ItemToPurchase("Nike Romaleos", 200, 3, "none")
        self.cart.modify_item(modified_item)
        
        # Find the modified item in the cart
        for item in self.cart.cart_items:
            if item.item_name == "Nike Romaleos":
                self.assertEqual(item.item_price, 200)
                self.assertEqual(item.item_quantity, 3)
                # Description should remain unchanged as default value was passed
                self.assertEqual(item.item_description, "Volt color, Weightlifting shoes")
                break
    
    def test_modify_item_not_found(self):
        """Test that proper message is displayed when modifying non-existent item"""
        modified_item = ItemToPurchase("NonExistentItem", 100, 1, "none")
        output = self.capture_output(self.cart.modify_item, modified_item)
        self.assertIn("Item not found in cart. Nothing modified.", output)
    
    def test_get_num_items_in_cart(self):
        """Test getting the total number of items in the cart"""
        # 2 Nike Romaleos + 5 Chocolate Chips = 7 items
        self.assertEqual(self.cart.get_num_items_in_cart(), 7)
    
    def test_get_cost_of_cart(self):
        """Test calculating the total cost of the cart"""
        # (2 * $189) + (5 * $3) = $378 + $15 = $393
        self.assertEqual(self.cart.get_cost_of_cart(), 393)
    
    def test_print_total_with_items(self):
        """Test printing the cart total with items"""
        output = self.capture_output(self.cart.print_total)
        self.assertIn("John Doe's Shopping Cart - May 11, 2025", output)
        self.assertIn("Number of Items: 7", output)
        self.assertIn("Nike Romaleos 2 @ $189 = $378", output)
        self.assertIn("Chocolate Chips 5 @ $3 = $15", output)
        self.assertIn("Total: $393", output)
    
    def test_print_total_empty_cart(self):
        """Test printing the cart total with an empty cart"""
        empty_cart = ShoppingCart("Jane Doe", "May 12, 2025")
        output = self.capture_output(empty_cart.print_total)
        self.assertIn("Jane Doe's Shopping Cart - May 12, 2025", output)
        self.assertIn("SHOPPING CART IS EMPTY", output)
    
    def test_print_descriptions_with_items(self):
        """Test printing item descriptions with items in cart"""
        output = self.capture_output(self.cart.print_descriptions)
        self.assertIn("John Doe's Shopping Cart - May 11, 2025", output)
        self.assertIn("Item Descriptions", output)
        self.assertIn("Nike Romaleos: Volt color, Weightlifting shoes", output)
        self.assertIn("Chocolate Chips: Semi-sweet", output)
    
    def test_print_descriptions_empty_cart(self):
        """Test printing item descriptions with an empty cart"""
        empty_cart = ShoppingCart("Jane Doe", "May 12, 2025")
        output = self.capture_output(empty_cart.print_descriptions)
        self.assertIn("Jane Doe's Shopping Cart - May 12, 2025", output)
        self.assertIn("SHOPPING CART IS EMPTY", output)


class TestMenuFunctionality(unittest.TestCase):
    """Test menu functionality with simulated user input"""
    
    def setUp(self):
        """Set up test fixtures before each test"""
        self.cart = ShoppingCart("Test User", "May 11, 2025")
    
    @patch('builtins.input', side_effect=['a', 'Test Item', 'Test Description', '10.99', '2', 'q'])
    def test_add_item_to_cart(self, mock_input):
        """Test adding an item to the cart through the menu"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_menu(self.cart)
        sys.stdout = sys.__stdout__
        
        # Check that the item was added to the cart
        self.assertEqual(len(self.cart.cart_items), 1)
        self.assertEqual(self.cart.cart_items[0].item_name, "Test Item")
        self.assertEqual(self.cart.cart_items[0].item_description, "Test Description")
        self.assertEqual(self.cart.cart_items[0].item_price, 10.99)
        self.assertEqual(self.cart.cart_items[0].item_quantity, 2)
    
    @patch('builtins.input', side_effect=['a', 'Item1', 'Desc1', '5', '1', 'r', 'Item1', 'q'])
    def test_remove_item_from_cart(self, mock_input):
        """Test removing an item from the cart through the menu"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_menu(self.cart)
        sys.stdout = sys.__stdout__
        
        # Check that the item was added and then removed
        self.assertEqual(len(self.cart.cart_items), 0)
    
    @patch('builtins.input', side_effect=['a', 'Item1', 'Desc1', '5', '1', 'c', 'Item1', '3', 'q'])
    def test_change_item_quantity(self, mock_input):
        """Test changing an item's quantity through the menu"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_menu(self.cart)
        sys.stdout = sys.__stdout__
        
        # Check that the item quantity was updated
        self.assertEqual(len(self.cart.cart_items), 1)
        self.assertEqual(self.cart.cart_items[0].item_quantity, 3)
    
    @patch('builtins.input', side_effect=['a', 'Item1', 'Desc1', '5', '1', 'i', 'q'])
    def test_output_item_descriptions(self, mock_input):
        """Test outputting item descriptions through the menu"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_menu(self.cart)
        sys.stdout = sys.__stdout__
        
        # Check that descriptions were output properly
        self.assertIn("Item Descriptions", captured_output.getvalue())
        self.assertIn("Item1: Desc1", captured_output.getvalue())
    
    @patch('builtins.input', side_effect=['a', 'Item1', 'Desc1', '5', '1', 'o', 'q'])
    def test_output_shopping_cart(self, mock_input):
        """Test outputting the shopping cart through the menu"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_menu(self.cart)
        sys.stdout = sys.__stdout__
        
        # Check that cart was output properly
        self.assertIn("Test User's Shopping Cart - May 11, 2025", captured_output.getvalue())
        self.assertIn("Item1 1 @ $5.0 = $5.0", captured_output.getvalue())
        self.assertIn("Total: $5.0", captured_output.getvalue())
    
    @patch('builtins.input', side_effect=['invalid', 'q'])
    def test_invalid_menu_option(self, mock_input):
        """Test handling of invalid menu options"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_menu(self.cart)
        sys.stdout = sys.__stdout__
        
        # Check that invalid option was handled properly
        self.assertIn("Invalid option", captured_output.getvalue())


class TestMainFunction(unittest.TestCase):
    """Test the main function with simulated user input"""
    
    @patch('builtins.input', side_effect=['John Smith', 'May 11, 2025', 'q'])
    def test_main_function_customer_info(self, mock_input):
        """Test that main function correctly prompts for customer info"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Customer name: John Smith", output)
        self.assertIn("Today's date: May 11, 2025", output)


if __name__ == "__main__":
    unittest.main()