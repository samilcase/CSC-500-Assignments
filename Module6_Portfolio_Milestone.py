class ItemToPurchase:
    
    def __init__(self, name = "none", price = 0.00,quantity = 0, description=''):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description


    def print_item_cost(self):
        print('{:<20} {:.0f} @ ${:.2f} = ${:>6.2f}'.format(self.name,self.quantity,self.price, self.quantity*self.price))

class ShoppingCart:
    def __init__(self,customer_name = 'none', current_date = 'January 1, 2020',cart_items=None):
        if cart_items is None:
            cart_items=[]
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):
        item_name = input('Enter item name: ')
        item_description = input('Enter item description: ')
        item_price = float(input("Enter the item\'s price: "))
        item_quantity = int(input('Enter the item\'s quantity: '))
        
        new_item = ItemToPurchase(item_name,item_price,item_quantity,item_description)

        self.cart_items.append(new_item)
        
    def remove_item(self):
        item_name = input('Enter item name to remove: ')
        found = False
        for item in self.cart_items:
            if item_name ==item.name:
                self.cart_items.remove(item)
                found = True
                break 
        if not found:
            print('Item not found in cart. Nothing removed.')
    
    def modify_item(self):
        #modifies an item's description?, price, and/or quanitity
        item_name = input('Enter item name to modify: ')
        found = False

        for item in self.cart_items:
            if item_name == item.name:
                found = True
                print('Modifying {}'.format(item_name))
                new_description = input('Enter new description for {} (current: {}) or press Enter to Keep'.format(item.name,item.description))
                new_price = input('Enter new price for {} (current: ${:.2f}) or press Enter to keep: '.format(item.name,item.price))
                new_quantity = input('Enter new quantity for {} (current: {}) or press Enter to keep: '.format(item.name,item.quantity))
                
                if new_description:
                    item.description = str(new_description)
                if new_price:
                    item.price = float(new_price)
                if new_quantity:
                    item.quantity = int(new_quantity)
                break

        if not found:
            print('Item not found in cart. Nothing modified.')


    def get_num_items_in_cart(self):
        count = 0

        for item in self.cart_items:
            count += item.quantity

        print('Number of items: {}'.format(count))

    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += item.quantity * item.price
        print('Total: ${:.2f}'.format(total_cost))

    def print_total(self):
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                item_cost = item.quantity * item.price
                print('{} {} @ ${} = ${}'.format(item.name,item.quantity,item.price,item_cost))

    def print_descriptions(self):
        print('Item Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.name,item.description))
    
def print_menu(cart):
    menu = (
    "\nMENU\n"
    "a - Add item to cart\n"
    "r - Remove item from cart\n"
    "c - Change item quantity\n"
    "i - Output items' descriptions\n"
    "o - Output shopping cart\n"
    "q - Quit\n"
    )

    command = ''
    while command != 'q':
        print(menu)
        command = input("Choose an option: ").strip().lower()

        if command == 'a':
            cart.add_item()
        elif command == 'r':
            cart.remove_item()
        elif command == 'c':
            cart.modify_item()
        elif command == 'i':
            cart.print_descriptions()
        elif command == 'o':
            print('\n{}\'s Shopping Cart - {}'.format(cart.customer_name,cart.current_date))
            cart.get_num_items_in_cart()
            cart.print_total()
            cart.get_cost_of_cart()
        elif command == 'q':
            print("Goodbye!")
        else:
            print("Invalid option. Please try again.")

def main():
    customer_name = input('Enter customer\'s name: ')
    current_date = input('Enter today\'s date: (e.g., January 1, 2024) ')
    cart = ShoppingCart(customer_name,current_date)

    print_menu(cart)

main()