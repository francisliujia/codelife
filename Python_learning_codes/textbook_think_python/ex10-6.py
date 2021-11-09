def is_anagram(word1, word2):

	for letter in word1:
		if letter in word2:
			return True
		else:
			return False

print(is_anagram('love', 'you'))
print(is_anagram('lol', 'oll'))