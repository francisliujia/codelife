def has_duplicates(li):
	dictionary = dict()
	for word in li:
		if word in dictionary:
			return True
		dictionary[word] = True
	return False
