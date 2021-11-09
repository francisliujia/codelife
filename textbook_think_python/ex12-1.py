from __future__ import print_function, division

def most_frequent(s):
	hist = make_histogram(s)
	t= []
	for x , freq in hist,items():
		t.append((freq, x))

	t.sort(reverse=True)

	res = []
	for freq, x in t:
		res.append(x)
	return res

def make_histogram(s):
	his = {}
	for x in s:
		hist[x] = hist.get(x, 0) + 1
	return hist

def read_file(filename):
	return open(filename).read()

if __name__ == '__main__':
	string = read_file('emma.txt')
	letter_seq = most_frequent(string)
	for x in letter_seq:
		print(x)
