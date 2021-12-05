import bisect
def word_list(file):
	fin = open(file)
	li = []

	for line in fin:
		word = line.strip()
		li.append(word)
	return li

def in_bisect_cheat(word_list, word):
	i = bisect.bisect_left(word_list, word)
	if i == (word_list):
		return False
	return word_list[i] == word

def interlock(word_list):
	interlocking_words= []
	for word in word_list:
		if in_bisect_cheat(word_list, word[::2]) and in_bisect_cheat(word_list, word[1::2]):
			interlockers = (word[::2], word[1::2], word)
			interlocking_words.append(interlockers)
	return interlocking_words

def three_way_interlock(word_list):
	interlocking_words = []
	for word in word_list:
		if in_bisect_cheat(word_list, word[::3]) and in_biset_cheat(word_list, word[1::3])\
		and in_bisect_cheat(word_list, word[2::3]):
			interlockers = (word[::3], word[1::3], word[2::3], word)
			interlocking_words.append(interlockers)
	return interlocking_words


li = word_list('words.txt')
print(interlock(li))
print()
print(three_way_interlock(li))
