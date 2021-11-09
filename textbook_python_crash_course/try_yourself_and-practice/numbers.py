

for number in range(1, 21, 2):
    print(number)

threes = range(3, 31, 3)
for number in threes:
    print(number)

numbers = range(1, 11)
for number in numbers:
    print(number**3)

cubes = [value**3 for value in range(1, 11)]

print(cubes)
