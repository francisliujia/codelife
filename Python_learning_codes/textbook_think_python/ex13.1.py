import string

def process_file(filename):
	hist = dict()
	fin = open(filename)
	for line in fin:
		process_line(line, hist) 
	return hist 

def process_line(line, hist):
	line = line.replace('-', ' ')

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		hist[word] = hist.get(word, 0) + 1

hist = process_file('aliece.txt')
print(hist)