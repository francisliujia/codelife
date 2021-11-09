
# f = open('testfile.txt')
try:
	f = open('currupt_file.txt')
	if f.name == 'currupt_file.txt':
		raise Exception

	# var = bad_var
	# pass


# except Exception:
# except FileNotFoundError:
except FileNotFoundError as e:
	print('error!')
	# print('sorry this file does not exist')
	# pass

except Exception as e:
	# print('sorry, something went wrong.')
	print(e)
else:
	print(f.read())
	f.close()
# will run no matter if exception happens or not 
finally:
	# pass
	print('executing finally')





# import sys
# print(sys.version)
