import csv
import zipfile
import shutil
import requests


# r = requests.get('https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2019.zip')
r = requests.get('https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2019.zip')

# with open('data_demo.zip', 'wb') as f:
# 	f.write(r.content)


with zipfile.ZipFile('data_demo.zip', 'r') as data_zip_file:
	data_zip_file.extractall('data_files')
