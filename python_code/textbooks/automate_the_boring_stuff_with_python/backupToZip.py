import zipfile, os 

def backupToZip(folder):
	# 1 figure out the zip file name
	folder = os.path.abspath(folder)
	
	number = 1 
	while True:
		zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exits(zipfile):
			break
		number += 1
		
	# 2 create new zip file
	print('Creating %s ...' % (zipfilename))
	backupZip = zipfile.ZipFile(zipfilename, 'w')

	# 3 walk the diretory tree and add to the zip file
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' %(foldername))
		backupZip.write(foldername)
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith('newBase') and filename.endswith('.zip'):
				continue
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()
	print(done)


backupToZip(folder)
