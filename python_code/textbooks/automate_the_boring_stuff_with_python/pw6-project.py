# ! python3
# pw6-project.py -- an insecure password locker program.

PASSWORD = {
	'email': 'qweurykhjadsbfkjg234132',
	'blog': 'asdfjkasj7231548',
	'luggage': 'asdjklfghadskj36752',
}

import sys
import pyperclip

if len(sys.argv) < 2:
	print('Usage: python pw6-project.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]

if account in PASSWORD:
	pyperclip.copy(PASSWORD[account])
	print('Password for '+ account +' copied to clipboard.')
else:
	print('There is no account names ' + account)