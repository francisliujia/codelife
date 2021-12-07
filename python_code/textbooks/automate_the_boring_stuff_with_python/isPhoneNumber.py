# def isPhonenumber(text):
# 	if len(text) != 12:
# 		return False
# 	for i in range(0, 3):
# 		if not text[i].isdecimal():
# 			return False
# 	if text[3] != '-':
# 		return False
# 	for i in range(4, 7):
# 		if not text[i].isdecimal():
# 			return False
# 	if text[7] != '-':
# 		return False
# 	for i in range(8, 12):
# 		if not text[i].isdecimal():
# 			return False
# 	return True

# # print('415-555-3232 is a number:')
# # print(isPhonenumber('415-555-3232'))
# # print('moshi moshi is a phone number:')
# # print(isPhonenumber('moshi moshi'))


# message = 'call me at 415-555-3232 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
# 	chunk = message[i: i+12]
# 	if isPhonenumber(chunk):
# 		print('Phone number found: ' + chunk)
# print('Done')

# print()


import re
# phoneNumRegx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegx.search('My phone number is 415-555-2323')
# print('Phone number found: ' + mo.group())

# print()

# phoneNumRegx = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo = phoneNumRegx.search('My phone number is 415-555-2323')


# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(3))
# print(mo.group())
# print(mo.groups())

# areacode, mainnumber, other = mo.groups() 
# print(areacode)
# print(mainnumber)
# print(other)


# phoneNumRegx = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegx.search('My phone number is (415) 555-2323.')
# print(mo.group(1))

# heroRegx = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegx.search('Batman and Tina Fey.')
# print(mo1.group())

# mo2 = heroRegx.search('Tina Fey and Batman.')
# print(mo2.group())


# batRegx = re.compile(r'Bat(man|mobile|coper|bat)')
# mo = batRegx.search('Batmobile lost a wheel.')
# print(mo.group())
# print(mo.group(1))


# batRegx = re.compile(r'Bat(wo)?man') 
# mo1 = batRegx.search('The adventures of Batman')
# print(mo1.group())

# mo2 = batRegx.search('The adventures of Batwoman')
# print(mo2.group())

# phoneRegx = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegx.search('My phone number is 415-555-4334')
# print(mo1.group())


# mo2 = phoneRegx.search('My phone number is 415-4334')
# print(mo2.group())


# batRegx = re.compile(r'Bat(wo)*man') 
# mo1 = batRegx.search('The adventures of Batman')
# print(mo1.group())

# mo2 = batRegx.search('The adventures of Batwoman')
# print(mo2.group())

# mo3 = batRegx.search('The adventures of Batwowowoman')
# print(mo3.group())

# batRegx = re.compile(r'Bat(wo)+man') 
# mo1 = batRegx.search('The adventures of Batman')
# print(mo1 == None)

# mo2 = batRegx.search('The adventures of Batwoman')
# print(mo2.group())

# mo3 = batRegx.search('The adventures of Batwowowoman')
# print(mo3.group())



# haRegx = re.compile(r'(ha){3}')
# mo1 = haRegx.search('hahaha')
# print(mo1.group())

# mo2 = haRegx.search('ha')
# print(mo2 == None)


# greedyhaRegx = re.compile(r'(ha){3,5}')
# mo1 = greedyhaRegx.search('hahahaha')
# print(mo1.group())


# greedyhaRegx = re.compile(r'(ha){3,5}?')
# mo1 = greedyhaRegx.search('hahahahaha')
# print(mo1.group())


# phoneNumRegx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegx.search('Cell: 415-555-6666 work 212-555-9999')
# print(mo.group())



# phoneNumRegx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo1 = phoneNumRegx.findall('Cell: 415-555-6666 work 212-555-9999')
# print(mo1)


# phoneNumRegx = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo1 = phoneNumRegx.findall('Cell: 415-555-6666 work 212-555-9999')
# print(mo1)


# xmasRegx = re.compile(r'\d+\s\w+')
# mo = xmasRegx.findall('12c drumers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, \
# 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(mo)


# vowlRegx = re.compile(r'[aeiouAEIOU]')
# mo = vowlRegx.findall('Rbocop eats baby food. BABY FOOD.')
# print(mo)

# vowlRegx = re.compile(r'[^aeiouAEIOU]')
# mo = vowlRegx.findall('Rbocop eats baby food. BABY FOOD.')
# print(mo)

# beginwithhgello = re.compile(r'^Hello')
# mo = beginwithhgello.search('Hello world')
# print(mo)
# 

# endswithnumber = re.compile(r'\d$')
# mo = endswithnumber.search('You number is 32')
# print(mo)

# wholestringisnum = re.compile(r'^\d+$')
# mo = wholestringisnum.search('1234566')
# print(mo)


# atRegx = re.compile(r'.at')
# mo = atRegx.findall('the cat in the hat sat on the flat mat.')
# print(mo)

# nameRegx = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegx.search('First Name: Al Last Name: Sweigart')
# print(mo)

# print(mo.group(1))
# print(mo.group(2))


# nongreedyRegx = re.compile(r'<.*?>')
# mo = nongreedyRegx.search('<To searve a man> for dinner.>')
# print(mo.group())


# nongreedyRegx = re.compile(r'<.*>')
# mo = nongreedyRegx.search('<To searve a man> for dinner.>')
# print(mo.group())



# nonewlineRegx = re.compile('.*')
# mo = nonewlineRegx.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
# print(mo.group())


# nonewlineRegx = re.compile('.*', re.DOTALL)
# mo = nonewlineRegx.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
# print(mo.group())



# robocop = re.compile(r'robocop', re.I)
# mo = robocop.search('Robocop is a good man.')
# print(mo.group())



# namesRegx = re.compile(r'Agent \w+')
# mo = namesRegx.sub('Censored', 'Agent Alice gave the secret documents to Agent Bob.')
# print(mo)


namesRegx = re.compile(r'Agent (\w)\w*')
mo = namesRegx.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

