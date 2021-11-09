import palindrome
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif palindrome.first(word) == palindrome.last(word):
        return True
        if len(palindrome.middle(word)) == 1:
            return True
        else:
            is_palindrome(palindrome.middle(word))
    else:
        return False
    
print(is_palindrome('hello'))
print(is_palindrome(''))
print(is_palindrome('kk'))
print(is_palindrome('lol'))
print(is_palindrome('noon'))

        