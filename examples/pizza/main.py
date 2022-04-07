""" a simple program to take a pizza order and print out the order ticket
d_choices
for the kitchen """

import pizzadata as pd

class Pizza:
    size = ''
    ingredients = []
    price = 0

    def __init__(self, size):
        self.size = size
        self.pd = pd.PizzaData()

    def full_price(self):
        """ returns full price of pizza, incl tax """
        

def take_order():
    """ interact with the cashier, and record the customer's order.  return
    the order information to the caller. """
    data = pd.PizzaData()
    sizes = data.sizes
    ingredients = data.ingredients

    while True:
        print('Available sizes')
        for i, size in enumerate(sizes):
            print(f'{i+1}: {size}')
        try:
            size = int(input('Choose a size: '))
        except ValueError:
            print('Please choose a number')
            continue
        num_sizes = len(sizes)
        # TODO: need to fix the returned value so it's a string and not a number
        if size > 0 and size <= num_sizes:
            break
        else:
            print('Please pick a real size')

    while True:
        print('Available ingredients:')
        for i, item in enumerate(ingredients):
            print(f'{i+1}: {item}')
        topping_choices = input('Choose your ingredients (no commas): ')
        good_choices = True
        num_items = len(ingredients)
        for choice in topping_choices:
            choice = int(choice)
            if choice <= 0 or choice > num_items:
                print(f'{choice} is not a recognized ingredient')
                good_choices = False

        #choices = topping_choices.split(', ')
        #good_choices = True
        #for choice in choices:
            #if choice not in ingredients:
                #print(f'{choice} is not a recognized ingredient')
                #good_choices = False
        if not good_choices:
            continue
        break

    order = {}
    order['size'] = size
    order['toppings'] = topping_choices
    return order

def do_print(*args, **kwargs):
    print("we're using a wrapper function!")
    print_order(*args, **kwargs)
    print("we're done with the wrapper!")

def print_order(order, extra_msg='', silly_msg='', ridiculous_msg=''):
    """ print out the order for the kitchen """
    data = pd.PizzaData()
    print('A new order has arrived! Huzzah!')
    print('Size:', data.sizes[int(order['size']) - 1])
    print('Toppings:')
    for choice in order['toppings']:
        print(data.ingredients[int(choice) - 1])
    size_index = int(order['size']) - 1
    price = data.prices[size_index]
    # note: the .tax method takes an index, not a price
    print(f'Price: {price} Tax: {data.tax(size_index)}')
    if extra_msg:
        print('extra message:')
        print(extra_msg)
    if silly_msg:
        print('silly message:')
        print(silly_msg)
    if ridiculous_msg:
        print('ridiculous message:')
        print(ridiculous_msg)


def main():
    order = take_order()
    do_print(order, silly_msg='Have a nice day!')

if __name__ == '__main__':
    main()
