import os

os.chdir('/Users/ji-axinliu/Downloads/BOOKS/p_books')

# print(os.getcwd())

for f in os.listdir():
	# print(f)
	# print(os.path.splitext(f))

	file_name, file_ext = os.path.splitext(f)
	# print(file_name)
	# print(file_name.split('-'))
	f_title, f_course, f_num = file_name.split('-')
	# print(f_title)
	# print(f_course)
	# print(f_num)
	f_course = f_course.strip()
	f_num = f_num.strip()[1:].zifill(2)

	new_name = '{}-{}{}'.format(f_num, f_title,file_ext)

	os.rename(f, new_name)

	# print('{}-{}-{}{}'.format(f_num, f_course, f_title,file_ext))