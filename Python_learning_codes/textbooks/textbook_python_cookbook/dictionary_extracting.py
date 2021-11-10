prices = {
	'acem': 45.23,
	'appl': 1223,
	'hpa': 123,
	'abs': 123.3,
}

p1 = {key:value for key,value in prices.items() if value > 100}
tech_names = {'appl', 'ibm', 'hqp', 'msft'}
p2 = {key:value for key, value in prices.items() if key in tech_names}

print(p1)
print(p2)