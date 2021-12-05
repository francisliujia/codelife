birthdays ={'Alice':'April 1', 'francis':'Jan 27', 'Tousef':'Dec 20','Jelmer':'May 20'}

while True:
	print('Please enter a name:(blank to quit)')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birthday info for ' + name)
		print('what is his or her birthday?')
		bday = input()
		birthdays[name] = bday
		print('birthdays database updated')