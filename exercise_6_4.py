toppings1 = ['onions', 'mozzarella', 'mushrooms']
pizza1 = {
    'size': 'small',
    'toppings': toppings1,
}

toppings2 = ['pepperoni', 'hamburger', 'sausage']
pizza2 = {
    'size': 'large',
    'toppings': toppings2,
}

toppings3 = ['barbecue chicken', 'basil', 'broccoli']
pizza3 = {
    'size': 'medium',
    'toppings': toppings3,
}

pizzas = [pizza1, pizza2, pizza3]

for instructions in pizzas:
    size = instructions['size']
    toppings = ', '.join(instructions['toppings'])
    toppings_string = ''
    for item in toppings:
        toppings_string += item + ', '
    print(f'Make a {size} pizza with the following toppings: {toppings_string}')
