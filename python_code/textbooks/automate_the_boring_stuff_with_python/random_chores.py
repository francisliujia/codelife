import random 
import smtplib 


def get_chore(email, last_chore):
	chore_list = chores[:]
	try:
		chore_list.remove(last_chore)
	except ValueError:
		pass
	if chore_list:
		new_chore = random.choice(chore_list)
		chore_assignments[email] = new_chore
		chores.remove(new_chore)
	else:
		print('Get new chore successfully')

def send_chore(email, chosen_chore):
	smtp_obj.sendmail('Example@mail.com', email, 'Subject: This week chore.'
						'\n You have been assigned ' + chosen_chore +
						'. You will not receive this chore next time')

with open('last_chore.txt') as f:
	last_chores = f.readlines()

EMAILS = ['recipient1@email.com,'
		  'recipient1@email.com,'
		  'recipient1@email.com,'
		  'recipient1@email.com,']

chore_assignments = {}

while len(chore_assignments) < 4:
	chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
	get_chore(EMAIL[0], last_chore[0].strip())
	get_chore(EMAIL[1], last_chore[1].strip())
	get_chore(EMAIL[2], last_chore[2].strip())
	get_chore(EMAIL[3], last_chore[3].strip())


smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_obj.ehlo()
smtp_obj.login('example@email.com', 'Password')

for address, chore in chore_assignments.items():
	send_chore(address, chore)

smtp_obj.quit()

with open('last_chores.txt', 'w') as f:
	f.write(chore_assignments[EMAIL[0]] + '\n')
	f.write(chore_assignments[EMAIL[1]] + '\n')
	f.write(chore_assignments[EMAIL[2]] + '\n')
	f.write(chore_assignments[EMAIL[3]] + '\n')

print('Everyone has been emailed their lastest chore -- Programm closed.')














