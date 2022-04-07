""" This class defines some static data we need for the running of our fancy 
pizza restaurant """

print('__name__ is set to: ' + __name__)

class PizzaData:
    """ This is the PizzaData class, whee! """
    sizes = ['small', 'medium', 'large']
    ingredients = ['onion', 'sausage', 'broccoli', 'bbq chicken', 'mushrooms',
        'mozzarella', 'tomatoes', 'basil', 'pesto']
    prices = [12.99, 15.99, 20.99]

    def tax(self, size):
        ''' this is the tax method, also cool'''
        tax_rate = 0.1
        return(self.prices[size] * tax_rate)
