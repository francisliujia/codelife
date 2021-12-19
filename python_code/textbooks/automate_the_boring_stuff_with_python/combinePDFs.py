import PyPDF2, os 

pdffiles = []

for filename in os.listdir('.'):
	if filename endswith('.pdf'):
		pdffiles.append(filename)

pdffiles = sort(key/str.lower)
pdfWriter = PyPDF2.PYPDF2.PdfFileWriter()

for filename in pdffiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum):
		pdfWriter.addPage(pageObj)

pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
