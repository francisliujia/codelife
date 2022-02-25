

with open('poem.txt', 'r') as f:
	# for line in f:
		# print(line)
	lines = f.readlines()
	# print(lines)
	clean_word = []
	for line in lines:
		# print(line)
		words = line.split(' ')

		for word in words:
			word = word.replace('\n', '')
			if word.endswith(','):
				word.replace(',', '')
			elif word.endswith(';'):
				word.replace(';', '')
			elif word.endswith('.'):
				word.replace('.', '')
			elif word.endswith(':'):
				word.replace(':', '')
			elif word.endswith('—'):
				word.replace('—', '')
			elif word.endswith('!'):
				word.replace('!', '')
			# elif word.endswith('\n'):
			# 	word.replace('\n', '') 
			clean_word.append(word)
# print(clean_word)

count = dict()
for word in clean_word:
	count.setdefault(word, 0)
	count[word] += 1

import pprint
# print(count)
pprint.pprint(count)

# word_count = {}
# with open("poem.txt","r") as f:
#     for line in f:
#         tokens = line.split(' ')
#         for token in tokens:
#             token=token.replace('\n','')
#             if token in word_count:
#                 word_count[token]+=1
#             else:
#                 word_count[token]=1
# print(word_count)


		# print(words)
		# for word in words:



# count = dict()
# for char in message:
# 	count.setdefault(char, 0)
# 	count[char] += 1

# import pprint
# # print(count)
# pprint.pprint(count)