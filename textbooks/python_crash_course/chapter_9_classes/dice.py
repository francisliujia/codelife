from random import randint

class Die():
    '''represent a dice, which could be rolled'''
    def __init__(self, sides=6):
        '''initialize the dice'''
        self.sides = sides

    def roll_die(self):
        '''return a random number between 1 and the number of sides'''
        return randint(1, self.sides)

d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a 6-side die")
print(results)

print("\n")

d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)

print("10 rolls of a 10-side die")
print(results)

print("\n")

d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)

print("10 rolls of a 20-side die")
print(results)