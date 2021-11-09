def rotated_word(word, size):
    rotated_word = ' '
    for letter in word:
        rotated_word += chr(ord(letter) + size)
    return rotated_word

print(rotated_word('love', 3))
print(rotated_word('Plamena', 2))
