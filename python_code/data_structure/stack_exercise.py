def reverse_str(string):
	return string[::-1]

# reversed = reverse_str('word is found')
# print(reversed)

from stack import Stack
from collections import deque

def reverse_string(s):
	stack = Stack()

	for char in s:
		stack.push(char)

	r_str = ''
	while stack.size() != 0:
		r_str += stack.pop()
	return r_str

# 'string' --> push --> 'string' --> pop -->'gnirts'

def is_matched(c1, c2):
	match_dict = {
	'}': '{',
	']': '[',
	')': '('
	}
	return match_dict[c1] == c2
res = is_matched(']', '[')
print(res)

print(res)
def is_balanced(s):
	stack = Stack()
	for char in s:
		if char == '(' or char=='{' or char=='[':
			stack.push(char)
		if char ==')' or char=='}' or char == ']':
			if stack.size() == 0:
				return False
			if not is_matched(char, stack.pop()):
				return False

	return stack.size() == 0
print(is_balanced('([])'))

def is_matched(c1, c2):
	match_dict = {
	'{': '}',
	'[': ']',
	'(': ')'
	}
	return match_dict[c1] == c2

print('my_match', is_matched('[', ']'))







