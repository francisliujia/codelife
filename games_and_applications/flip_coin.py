import random

def count_coin(num):
	heads_count = 0
	tails_count = 0
	
	for i in range(num):
		flip_result = random.randint(0,1)
		if flip_result == 1:
			heads_count += 1
		else:
			tails_count += 1
	return heads_count, tails_count


print('I will return the result of fliping a coin.')
do_loop = True
while do_loop:
	num = input('How many times do you want me to flip?')
	try:
		num = int(num)
		do_loop = False
	except Exception:
		print('Invalid input.\nYou need to input an integer.')
		do_loop = True


heads_count, tails_count = count_coin(num)
total_flips = heads_count + tails_count
head_pec = heads_count / total_flips
tail_pec = tails_count / total_flips
print(f'The flip result is total{total_flips}\n\
	heads {heads_count}: {round(head_pec, 10)}\n\
	tails {tails_count}: {round(tail_pec, 10)}')





