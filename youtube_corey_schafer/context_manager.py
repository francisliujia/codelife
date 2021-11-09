import os
from contextlib import  contextmanager

# cwd = os.getcwd()
# os.chdir('Sample_Dir_One')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('Sample_Dir_Two')
# print(os.listdir())
# os.chdir(cwd)



@contextmanager
def change_dir(destination):
	try:
		cwd = os.getcwd()
		os.chdir(destination)
		yield
	finally:
		os.chdir(cwd)


with change_dir('Sample-Dir_One'):
	print(os.listdir())

with change_dir('Sample-Dir_Two'):
	print(os.listdir())
