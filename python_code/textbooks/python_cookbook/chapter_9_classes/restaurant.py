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
