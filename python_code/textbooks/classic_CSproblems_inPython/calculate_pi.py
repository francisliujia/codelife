def calculate_pi(n_terms):
	numerator = 4
	demominator = 1
	operation = 1 
	pi = 0

	for _ in range(n_terms):
		pi += operation * (numerator/ demominator)
		demominator += 2
		operation *= -1
	return pi 

ret = calculate_pi(1000)
print(ret)
