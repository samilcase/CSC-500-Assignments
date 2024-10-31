
class ItemToPurchase:
    
    def __init__(self, name = "none", price = 0.00,quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity


    def print_item_cost(self):
        print('{} {:.0f} @ ${:.2f} = ${:.2f}'.format(self.name,self.quantity,self.price, self.quantity*self.price))

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
