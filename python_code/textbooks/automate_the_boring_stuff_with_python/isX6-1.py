while True:
	print("Please enter your age")
	age = input()
	if age.isdecimal():
		break
	else:
		print('you need to enter a numer.')

while True:
	print("Select a new password(letters and numbers only):")
	passsword = input()
	if passsword.isalnum():
		break
	else:
		print("passsword can only contain letters and numbers")



