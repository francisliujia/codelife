import PyPDF2

print('Enter the absolute path directory of the pdf you wish to creak:')
file = input()

with open('dictionary.txt') as f:
	words = f.readlines()
	pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))

	for word in words:
		word = word.strip()
		lower = word.lower()
		upper = word.upper()
		if pdf_reader.decrypt(lower) == 1:
			print('Password = ' + lower)
			break
		elif pdf_reader.decrypt(upper) ==1:
			print('Password = ' + upper)
			break
