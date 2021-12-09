import re 

def pasword_dection(password):
	if len(password) < 8:
		return False

	elif re.search('[0-9]', password) is None:
		return False
	elif re.search('[A-Z]', password) is None:
		return False
	elif re.search('[a-z]', password) is None:
		return False
	else:
		return 'Good password'

# pass = 123456677
nm = '13221gjfffF4132423'
# pasword_dection('q123151325')
ret =pasword_dection(nm)
print(ret)
