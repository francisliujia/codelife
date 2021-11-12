from random import randint

def date_generator(pupils):
	dates = []
	for student in range(pupils):
		dates.append(randint(1, 356))
	return dates

def has_matches(dates):
	dates.sort()
	for i in range(len(dates) - 1):
		if dates[i] == dates[i + 1]:
			return True
	return False

def chances(num_of_simulations, pupils):
	matches = 0

	for i in range(num_of_simulations):
		dates = date_generator(pupils)
		if has_matches(dates):
			matches += 1

	print(f"There are {matches} students have the same birthdays.")
	print(f"in {num_of_simulations} simulations.")

chances(1000, 23)