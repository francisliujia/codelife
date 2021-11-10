def read_dictionary(filename='c06d.txt'):
	d = dict()
	fin = open(filename)
	for line in fin:
		if line[0] == '#': continue

		t = line.split()
		word = t[0].lower()
		pron = ' '.join(t[1:])
		d[word] = pron
	return d

def word_hunter(word, dictionary):
	if word in dictionary:
		return True
	return False

def homophones(word_dict):
	li = []
	for word in word_dict:
		homophone1 = word[1::]
		homophone2 = word[0] + word[2:]

		if word_hunter(homophone1, word_dict) and word_hunter(homophone2, word_dict):
			if word_dict[word] == word_dict[homophone1] and word_dict[word] == word_dict[homophone2]:
				li.append(word)
	return li
dictionary = read_dictionary()
t = homophone(dictionary)

def make_dict(file_input):
	dictionary = dict()
	word_list = []

	fin = open(file_input)
	for line in fin:
		word = line.strip()
		word_list.append(word)

	index += 1

	return dictionary

word_list = make_dict('words.txt')
for word in t:
	if len(word) == 5 and word_hunter(word, word_list):
		print(word)



















