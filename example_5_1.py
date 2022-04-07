make_pizza = True
paid = False
ingredients = ['onion', 'pepper', 'mozarella']
stock = ['onion', 'mozarella', 'sauce', 'sausage']

# First, check that we have all the ingredients on hand
for ingredient in ingredients:
    if ingredient not in stock:
        print('setting make_pizza to false')
        make_pizza = False

# Then, independently, check to make sure we've been paid
if not paid:
    make_pizza = False

if make_pizza:
    print("Ok, we're ready to make your pizza")
else:
    print("Unfortunately, we're not ready to make your pizza just yet")
