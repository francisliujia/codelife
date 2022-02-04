import re

text_to_search = '''

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):

. ^ $ * + ? { } [ ] \ | ( )

coreyms.com
321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

urls = '''

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.com

'''

pattern = re.compile(r'https?://(www\.?)\w+\.\w+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)






sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start')

# use an ignore flag I
pattern = re.compile(r'start', re.I)

# or use an ignore flag IGNORECASE 
pattern = re.compile(r'start', re.IGNORECASE)

# only search and match the first string
matches = pattern.match(sentence)



matches = pattern.search(sentence)

print(matches)

# print('\tTab')
# print(r'\tTab')

# pattern = re.compile(r'abc')
# pattern = re.compile(r'.')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches number from 1 to 5
pattern = re.compile(r'[1-5]')

# matches char from a to z
pattern = re.compile(r'[a-z]')
# matches char from a to z and A to Z
pattern = re.compile(r'[a-zA-Z]')

#  matches everything is not from a-z and A-Z
pattern = re.compile(r'[^a-zA-Z]')
#  match any that not starts with b and followed by a and t
pattern = re.compile(r'[^b]at')
# matches -or a. as delimer
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# same as pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

#  stil only matches only one character
pattern = re.compile(r'\d\d\d[A-Za-z0-9-.]\d\d\d[-.]\d\d\d\d')

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# \. means match the exact . in the string
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')


matches = pattern.findall(text_to_search)


# only the groups are printed
for match in matches:
	print(match)

# to match a email address
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

matches = pattern.finditer(text_to_search)

# for match in matches:
# 	print(match)

with open('data.txt', 'r', encoding='utf-8') as f:
	contents = f.read()

	matches = pattern.finditer(text_to_search)

	for match in matches:
		print(match)




# print(text_to_search[2:5])
















