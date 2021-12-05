i = 0
numbers = []
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i += 1
    print("Number now", numbers)
    print(f"At the buttom i is {i}")

print("the numbers: ")
for num in numbers:
    print(num)