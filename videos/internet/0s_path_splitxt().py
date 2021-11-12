# Python program to explain os.path.splitext() method
	
# importing os module
import os

# path
path = '/home/User/Desktop/file.txt'

# Split the path in
# root and ext pair
root_ext = os.path.splitext(path)

# print root and ext
# of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1], "\n")


# path
path = '/home/User/Desktop/'

# Split the path in
# root and ext pair
root_ext = os.path.splitext(path)

# print root and ext
# of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1])
