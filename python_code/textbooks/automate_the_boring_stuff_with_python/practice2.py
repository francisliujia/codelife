# def collatz(number):
# 	if number % 2 == 0:
# 		return print(number // 2)
# 	elif number % 2 == 1:
# 		return print(3 * number + 1)


# collatz(44)

def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 ==1:
		return 3 * number + 1



num = int(input("please enter an integer:"))

result = collatz(num)
while result != 1:
		result = collatz(result)
		print(result)



