import zipfile

# my_zip = zipfile.ZipFile('files.zip', 'w')
# my_zip = zipfile.ZipFile('files.zip', 'w')
# my_zip.write('test.txt',)
# my_zip.write('comic.png',)

# my_zip.close()


# with zipfile.ZipFile('files.zip', 'w') as my_zip:
# 	my_zip.write('test.txt',)
# 	my_zip.write('comic.png',)


# with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
# 	my_zip.write('test.txt')
# 	my_zip.write('comic.png')



# with zipfile.ZipFile('files.zip', 'r') as my_zip:
# 	# print(my_zip.namelist())
# 	my_zip.extractall('files')

import shutil
# shutil.make_archive('another','zip', 'files')
# shutil.make_archive('another','gztar', 'files')

# shutil.unpack_archive('another.zip', 'another')
# shutil.unpack_archive('another.tar.gz', 'another2')

import requests

# r = requests.get('https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip')
# with open('data.zip','wb') as f:
# 	f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
	# print(data_zip.namelist())
	data_zip.extractall('data')









