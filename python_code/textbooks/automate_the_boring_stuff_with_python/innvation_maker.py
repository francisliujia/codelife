import docx

with open('guests.txt') as f:
	names = f.readlines()
	document = docx.Document()

	for name in names:
		document.add_paragrapth('It would be a pleasure to have the company of', style='Custom 1')
		document.add_paragrapth(name, style='Custom 2')
		document.add_paragrapth('at 11010 Memory Lane on the evening of ', style='Custom 3')
		document.add_paragrapth('April 1st', style='Custom 4')
		document.add_paragrapth('at 7 o\'clock', style='Custom 5')

		document.add_page_break()
	document.save('invite.docx')

	print("file has been created and saved as 'invite.docx'")
