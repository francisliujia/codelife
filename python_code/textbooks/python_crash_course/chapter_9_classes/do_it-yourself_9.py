''''
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.name} serves wonderful {self.cusine_type}.")

    def open_restaurant(self):
        print(f'{self.name} is open. Go get in!')


restaurant = Restaurant('green gates', 'pizza')
print(restaurant.name)
print(restaurant.cusine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

baby_baby = Restaurant('naked attraction', 'grilled pussies')
baby_baby.describe_restaurant()

hello_stranger = Restaurant('hello stranger', 'fried nipples')
hello_stranger.describe_restaurant()
'''

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cusine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.name} serves wonderful {self.cusine_type}.")

    def open_restaurant(self):
        print(f'{self.name} is open. Go get in!')


    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    '''represent a ice cream stand'''
    def __init__(self,name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        '''display the flavors available.'''
        print("We have the following flavours available: ")
        for flavor in self.flavors:
            print(f"-{flavor}")


lee_home = IceCreamStand('flavor king', 'ice cream')
lee_home.describe_restaurant()
lee_home.flavors = ['chocolate', 'cum water', 'breast spring']
lee_home.show_flavors()
