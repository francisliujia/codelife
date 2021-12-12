import re, os 

def search_folder(folder_path):
	target_file_list = []
	file_list = os.listdir(folder_path)
	for file in file_list:
		if file.endswith('.txt'):
			target_file_list.append(file)

	return target_file_list



def search_file(folder_path, files_list):
	file_path_list = []
	for file in file_list:
		file_path = os.path.join(folder_path, file)
		file_path_list.append(file_path)
	return file_path_list


def search_content_in_file(file_path_list, search_content):
	line_with_search_content = []
	for file in file_path_list:
		with open(file, 'r') as f:
			lines = f.readlines()
			for line in lines:
				if search_content in line:
					line_with_search_content.append(line)

	return line_with_search_content



	