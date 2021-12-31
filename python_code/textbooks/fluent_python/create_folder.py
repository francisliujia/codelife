# __author__ = 'francisaboutlee@gmail.com'
import os, re

current_path = os.path.abspath('.')
chapter_ls = ['chapter_'+ str(i) for i in range(1, 22)] 

# chapter_ls= list()
# for i in range(1, 22):
# 	chapter = 'chapter' + str(i)
# 	chapter_ls.append(chapter)


print(chapter_ls)

for dir_path in chapter_ls: 
	path = os.path.join(current_path, dir_path)
	os.makedirs(path)

