# This program implements a shopping cart system allowing users to add, remove, 
# and modify items in their cart

class ItemToPurchase:
    # This class represents an item that can be purchased
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        # Constructor that initializes an item with default values if not provided
        # Parameters:
        #   item_name: String representing the name of the item
        #   item_price: Integer or float representing the price of the item
        #   item_quantity: Integer representing how many of this item
        #   item_description: String describing the item
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

class ShoppingCart:
    # This class represents a shopping cart that can contain multiple items
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Constructor that initializes a shopping cart with customer information
        # Parameters:
        #   customer_name: String representing the customer's name
        #   current_date: String representing the current date
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # Empty list to store items in the cart
    
    def add_item(self, item):
        # Adds an ItemToPurchase object to the cart_items list
        # Parameters:
        #   item: An ItemToPurchase object to add to the cart
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        # Removes an item from cart_items list based on the item name
        # Parameters:
        #   item_name: String representing the name of item to remove
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item):
        # Modifies an existing item in the cart
        # Only modifies attributes that are not default values
        # Parameters:
        #   item: An ItemToPurchase object with the same name as an existing item
        #         but with updated attributes
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                found = True
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        # Calculates and returns the total quantity of all items in the cart
        # Returns:
        #   Integer representing the total quantity of all items
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        # Calculates and returns the total cost of all items in the cart
        # Returns:
        #   Float or integer representing the total cost
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        # Prints the total cost and details of all items in the cart
        # If the cart is empty, prints a message indicating that
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}")
        print()
        print(f"Total: ${self.get_cost_of_cart()}")
    
    def print_descriptions(self):
        # Prints the descriptions of all items in the cart
        # If the cart is empty, prints a message indicating that
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    # Displays a menu of options for the user to interact with the shopping cart
    # Parameters:
    #   cart: A ShoppingCart object to perform operations on
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ")
        if choice in ['a', 'r', 'c', 'i', 'o', 'q']:
            if choice == 'a':
                print("\nADD ITEM TO CART")
                item_name = input("Enter the item name: ")
                item_description = input("Enter the item description: ")
                item_price = int(input("Enter the item price: "))
                item_quantity = int(input("Enter the item quantity: "))
                item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                cart.add_item(item)
                
            elif choice == 'r':
                print("\nREMOVE ITEM FROM CART")
                item_name = input("Enter name of item to remove: ")
                cart.remove_item(item_name)
                
            elif choice == 'c':
                print("\nCHANGE ITEM QUANTITY")
                item_name = input("Enter the item name: ")
                new_quantity = int(input("Enter the new quantity: "))
                
                # Create a temporary item with default values but the new quantity
                item = ItemToPurchase(item_name, 0, new_quantity, "none")
                cart.modify_item(item)
                
            elif choice == 'o':
                print("\nOUTPUT SHOPPING CART")
                cart.print_total()
            elif choice == 'i':
                print("\nOUTPUT ITEMS' DESCRIPTIONS")
                cart.print_descriptions()
            elif choice == 'q':
                break
        else:
            print("Invalid option. Please try again.")

def main():
    # Main function to test the shopping cart functionality
    # Creates a sample cart and adds sample items for testing
    cart = ShoppingCart("John Doe", "February 1, 2020")
    
    # Add sample items for testing
    item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Volt color, Weightlifting shoes")
    item2 = ItemToPurchase("Chocolate Chips", 3, 5, "Semi-sweet")
    item3 = ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Bluetooth headphones")
    
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    
    # Start the menu
    print_menu(cart)

if __name__ == "__main__":
    main()