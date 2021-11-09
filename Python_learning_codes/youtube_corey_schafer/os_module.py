import os
from datetime import datetime

# print(dir(os))
# print(os.getcwd())

os.chdir('/Users/ji-axinliu/Downloads/python_programming/')

# print(os.getcwd())

# 'telusko-2'


# os.mkdir("telusko-2")
# os.rmdir('telusko-2')
# os.makedirs('telusko-2/sub-dir-1')
# os.removedirs('telusko-2/sub-dir-1')

# os.mkdir('test.txt')
# os.rename('test.txt', 'demo.txt')

# mode_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mode_time))

# print(os.stat('demo.txt').st_mtime)

# print(os.listdir())

# for dirpath, dirnames, filenames in os.walk('/Users/ji-axinliu/Downloads/python_programming/'):
# 	print('current path:', dirpath)
# 	print('directories:', dirnames)
# 	print('files:', filenames)
# 	print()


# print(os.environ)
# print(os.environ.get('HOME'))

# file_path = os.environ.get('HOME') + 'text.txt'

# this fixed the missing slash / issues
# file_path = os.path.join(os.environ.get('HOME'), 'text.txt')


# print(file_path)

# 'test.txt'


# print out the basename of the entire path
# print(os.path.basename('/tmp/test.txt'))

# # print out the dir name
# print(os.path.dirname('/tmp/test.txt'))

# # print both dir name and basename
# print(os.path.split('/tmp/test.txt'))

# # check if the file exists
# print(os.path.exists('/tmp/test.txt'))

# print(os.path.isdir('/tmp/test'))

# print(os.path.isfile('/tmp/test'))


# the file name without extention and the extention 
# print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))

























