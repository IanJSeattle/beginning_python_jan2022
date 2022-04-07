normal = ['olives', 'onions', 'mozzarella', 'garlic', 'sauce']
now = ['onions', 'sauce']

request = input('what ingredient would you like on your pizza? ')

if request in now:
    print(f'yes, we have {request} available!')
elif request in normal:
    print(f'sorry, normally we have {request}, but not right now.')
else:
    print(f"sorry, we don't have {request}, and don't usually stock it.")

print('finished making decision')
