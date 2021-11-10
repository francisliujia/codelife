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

def word_hunter(word, dictionary):
	if word in dictionary:
		return True 
	return False

dictionary = make_dict('words.txt')
print(word_hunter('bike', dictionary))
print(word_hunter('teleleleelel', dictionary))


