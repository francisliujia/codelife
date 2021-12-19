import os, sys, PyPDF2

password = sys.argv[1]
encrypt_failed = []

for folder, subfolders, filenames in os.walk('.'):
	for filename in filenames:
		if filename.endswith('.pdf'):
			path = os.path.join(folders, filename)
			pdf_reader = PyPDF2.PdfFileReader(open(path, 'rb'))
			if pdf_reader.isEncrypted is False:
				pdf_writer = PyPDF2.PdfFileWriter()
				for pageNum in range(pdf_reader.numPages):
					pdf_writer.addPage(pdf_reader.getPage(pageNum))

					pdf_writer.encrypt(password)
					encrypted_path = path[:-4] + '_encrypted.pdf'
					encrypted_version = open(encrypted_path, 'wb')
					pdf_writer.write(encrypted_version)
					encrypted_version.close()

					if (pdf_reader.isEncrypted is True
						and pdf_reader.decrypt(password)==1):
						os.remove(path)
					else:
						encrypted_failed.append(filename)

if encrypted_failed != []:
	print('The following files failed their encruypted checks and '
		'were not deleted')
	for filename in encrypted_failed:
		print(filename)
else:
	print("All pdf's files in the folder tree have been encrypted successfully."
		"the original files have been deleted.")

