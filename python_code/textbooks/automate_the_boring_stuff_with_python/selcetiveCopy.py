def selectiveCopy(folder, extension, new_folder):
	#1 walk the folder
	folder = os.path.abspath(folder)
	new_folder = os.path.abspath(folder)

	for foldername, subfolders, filenames in os.walk(folder):
		for subfolder in subfolders:
			for filename in filenames:
				if filename endswith(extension):
					shutil.copy(filename, new_folder)


def delete_unneeded_files(folder, size):
	folder = os.path.abspath(folder)			
	file_info = {}
	for foldername, subfolders, filenames in os.walk(folder):
		for subfolder in subfolders:
			for filename in filenames:
				file_size = os.path.getsize(filename)
				if file_size > size:
					filename = os.path.abspath(filename)
					file_info[filenames] = file_size

	print(file_info)


def close_gaps(folder, preFix):
	pass