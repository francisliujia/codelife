import re 

def stringRegx(string, rmString=None):
	if rmString == None:
		return string.strip()
	else:
		string = string.strip()
		string_Regx = re.compile(rmString)
		return string_Regx.sub('', string)


result = stringRegx('  dsafjjdsa fjlk sajdflk ', 'j')
print(result)
