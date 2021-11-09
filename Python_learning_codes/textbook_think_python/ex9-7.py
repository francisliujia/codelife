def searched_word(word):
	count = 0
	index = 0
	while index < len(word) - 1:
		if word[index] == word[index + 1]:
			count += 1
			if count == 3:
				return True
			index += 2
		else:
			count = 0
			index += 1

fin = open('words.txt')
count = 0
for line in fin:
	word = line.strip()
	if searched_word(word) == True:
		print(word)
		count += 1
print(count)
