import os, sys, PyPDF2

password = sys.argv[1]
decrypt_failed = []

for folders, subfolders, filenames in os.walk('.'):
	for filename, in filenames:
		path = os.path.join(folders, filename)
		pdf_reader= PyPDF2.PdfFileReader(open(path, 'rb'))
		if pdf_reader.isEncrypted:
			if pdf_reader.decrypt(password) != 1:
				print(filename + 'failed to decrypted')
				decrypt_failed .append(filename)

			else:
				pdf_writer = PyPDF2.PdfFileWriter()
				for pageNum in range(pdf_reader.numPages):
					pdf_writer.addPage(pdf_reader.getPage(pageNum))

				decrypted_path = path[:-4] + '_decrypted.pdf'
				decrypted_version = open(decrypted_path, 'wb')
				pdf_writer.write(decrypted_version)
				decrypted_version.close()

if decrypt_failed != []:
	print("all PDF's except those listed  above, were"
		"decrypted  successfully. All of the original files have been kept")
else:
	print("all encrypted PDF's in the folder tree were decrypted successfully."
		"the original files have been kept.")