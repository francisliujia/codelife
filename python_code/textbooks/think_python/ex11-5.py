def make_dict(file_input):
	dictionary = dict()
	word_list = []

	fin = open(file_input)
	for line in fin:
		word = line.strip()
		word_list.append(word)

	index = 0
	for word in word_list:
		dictionary[word] = index
		index += 1
	return dictionary

def rotate_word(word, shift):
	rotate_word = ' '
	for letter in word:
		rotate_word += chr(ord(letter) + shift)
	return rotate_word

def rotate_pairs(word_dict):
	pairs = {}
	for letter in range(1, 27):
		for word in word_dict:
			if rotate_word(word, letter) in word_dict:
				pairs[word].append((rotate_word(word, letter), letter))
			else:
				pairs[word] = [(rotate_word(word, letter), letter)]
	return pairs

dictionary = make_dict('words.txt')
print(rotate_pairs(dictionary))

