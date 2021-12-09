import pyperclip, re

phoneRegx = re.compile(r'''(
	(\d{3}|\(\d{3}\))?                    # area code
	(\s|-|\.)?			                # seperator
	(\d{3})				                # first three digits
	(\s|-|\.)			                # seperator
	(\d{4})				                # last three digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?)		# extension
	''', re.VERBOSE)


emailRegx = re.compile(r'''(
	[a-zA-Z0-9._%+-]+   # username
	@					# @ symbol
	[a-zA-Z0-9._]+		# domain name
	(\.[a-zA-Z]{2,4})	# dot-something
	)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegx.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' X' + groups[8]
	matches.append(phoneNum)

for groups in emailRegx.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')