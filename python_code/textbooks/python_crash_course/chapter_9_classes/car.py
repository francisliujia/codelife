class Car:
    '''a single attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    '''a simple attempt to model a battery for an electric car.'''
    def __init__(self, battery_size = 75):
        '''initialize the battery's attributes'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''print a statement describing the battery size.'''
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        '''print a statement about the range this battery provides.'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    '''represent aspects of a car, specific to electric vehicles'''

    def __init__(self, make, model, year):
        '''initialize attributes of the parent class
        then initialize attributes specific to an electric car'''
        super().__init__(make, model, year)
        self.battery = Battery()