#
#Sami Case
#CSC500 Module 4 Portfolio Milestone
#Created: October 30, 2024

#Assignment Prompt
#-------------------
# Online Shopping Cart
# Step 1: Build the ItemToPurchase class with the following specifications:

# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()
# Example of print_item_cost() output:
# Bottled Water 10 @ $1 = $10


# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

# Example:

# Item 1

# Enter the item name:

# Chocolate Chips

# Enter the item price:

# 3

# Enter the item quantity:

# 1

# Item 2

# Enter the item name:

# Bottled Water

# Enter the item price:

# 1

# Enter the item quantity:

# 10


# Step 3: Add the costs of the two items together and output the total cost.

# Example:

# TOTAL COST

# Chocolate Chips 1 @ $3 = $3

# Bottled Water 10 @ $1 = $10

# Total: $13

# Source Code:
# -------------------


class ItemToPurchase:
    
    def __init__(self, name = "none", price = 0.00,quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity


    def print_item_cost(self):
        print('{:<20} {:.0f} @ ${:.2f} = ${:>6.2f}'.format(self.name,self.quantity,self.price, self.quantity*self.price))

def main():
    total_cost = 0.0
    items = []
    
    num_items = int(input('Enter the number of items: '))
    
    for i in range(num_items):
        print('\nItem {}'.format(i+1))
        name = input('Enter the item name: ')
        price = float(input('Enter the item price: $'))
        quantity = int(input('Enter the item quantity: '))
        item = ItemToPurchase(name, price, quantity)
        items.append(item)
        total_cost += item.price * item.quantity

    print('\nTOTAL COST')
    for item in items:
        item.print_item_cost()
    print('\nTotal: ${:.2f}'.format(total_cost))

main()

