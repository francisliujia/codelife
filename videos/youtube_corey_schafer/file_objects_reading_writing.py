# file objects

# open the file

# use the context manager, then you don't need to worry about the closure
# automatically take care of the cleaning for us
# with open('test.txt', 'r') as f:
	# pass
	# f_contents = f.read()
	# print(f_contents, end='')

	# # using for loop fix the  memory issues, overloaded
	# # only read one line at a time
	# for line in f:
	# 	print(line, end='')


	# specify the amount of data we want to read at a time by passing in a 
	# size as a agguement

	# # here print out the first 100 chars of the file, instead all at once 
	# f_contents = f.read(100)
	# print(f_contents, end='')

	# # read the next 100 chars
	# f_contents = f.read(100)
	# print(f_contents, end='')





	# size_to_read = 10

	# f_contents = f.read(size_to_read)

	# while  len(f_contents) > 0:
	# 	print(f_contents, end='*')
	# 	f_contents = f.read(size_to_read)




	# # the second chunk picked up the tenth position and read the rest 10 chars
	# size_to_read = 10

	# f_contents = f.read(size_to_read)
	# print(f_contents, end='*')


	# f_contents = f.read(size_to_read)
	# print(f_contents)


	# now we want the second read to start at the beginning of the file

	# size_to_read = 10

	# f_contents = f.read(size_to_read)
	# print(f_contents, end='*')

	# # use seek() to achieve this

	# f.seek(0)

	# f_contents = f.read(size_to_read)
	# print(f_contents)





	# print(f.tell())


	# f_contents = f.readlines()
	# f_contents = f.readline()
	# print(f_contents)
	
	# f_contents = f.readline()
	# print(f_contents)

# f = open('test.txt', 'r')

# # print the name of the file
# print(f.name)

# # print out the mode of the file, now is in reading mode
# print(f.mode)

# # close the file
# f.close()

# print(f.closed)
# print(f.read())



# with open('test2.txt', 'w') as f:
# 	# pass
# 	f.write('Test')
# 	# using seek() will overwirte the remaining file
# 	f.seek(0)
# 	f.write('Test')


# with open('test.txt', 'r') as rf:
# 	with open('test_copy.txt', 'w') as wf:
# 		for line in rf:
# 			wf.write(line)



# copy a jpg file/ image

# with open('test.jpg', 'rb') as rf:
# 	with open('test_copy.jpg', 'wb') as wf:
# 		for line in rf:
# 			wf.write(line)



with open('test.jpg', 'rb') as rf:
	with open('test_copy.jpg', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)



