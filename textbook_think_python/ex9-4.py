def avoid(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

fin = open('words.txt')
count = 0

forbidden_letters = input("Type frobidden letters: ")

for line in fin:
    word = line.strip()
    if avoid(word, forbidden_letters) == True:
        count += 1

print(count)
