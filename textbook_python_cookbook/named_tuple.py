from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'share', 'price'])

def computer_cost(records):
	total = 0.0
	for rec in records:
		s = Stock(*rec)
		total += s.share*s.price
	return total
	