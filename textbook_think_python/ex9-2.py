def has_no_e(word):
    for letter in word:
        if letter =='e':
            return False
    return True
    
# print(has_no_e('love'))
# print(has_no_e('function'))
# print(has_no_e('gig'))

fin = open('words.txt')
count = 0
num_of_words = 110441

for line in fin:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)
print(count / num_of_words * 100, '%')
