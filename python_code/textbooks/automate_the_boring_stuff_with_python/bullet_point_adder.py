import pyperclip

text = pyperclip.paste()

pyperclip.copy(text)

lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '*' + lines[i]

pyperclip.copy(text)