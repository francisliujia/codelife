cars = 100
space_in_a_car = 4.0
drivers = 30
passagers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passagers / cars_driven

print("There are", cars, "care avaiable.")
print("There are only", drivers, "drivers avaiable.")
print("There will be", car_not_driven, "empty care today.")
print("We can transport", carpool_capacity, "empty cars today.")
print("We have", passagers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
        "in each car.")
