# This is a class to store information about an item in our shopping cart
class ItemToPurchase:
    # This is the constructor that sets up a new item
    def __init__(self):
        # Start with no name, price of 0, and quantity of 0
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
    
    # This function prints the cost of one item
    def print_item_cost(self):
        # Calculate total cost for this item (price times quantity)
        total = self.item_price * self.item_quantity
        # Print in the format: Name Quantity @ $Price = $Total
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")

# This is the main part of our program
def main():
    # Let the user know we're starting with item 1
    print("Item 1")
    
    # Create a new item for the first thing
    item1 = ItemToPurchase()
    # Ask the user for the item details
    item1.item_name = input("Enter the item name:\n")
    # Convert price to a number with decimals (float)
    item1.item_price = float(input("Enter the item price:\n"))
    # Convert quantity to a whole number (int)
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    
    # Now do the same for item 2
    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    
    # Show the final results
    print("\nTOTAL COST")
    # Print costs for both items
    item1.print_item_cost()
    item2.print_item_cost()
    
    # Add up the total cost (price * quantity for each item)
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    # Show the final total
    print(f"Total: ${total_cost:.0f}")

# This line starts our program
if __name__ == "__main__":
    main()