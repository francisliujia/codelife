# Python program to demonstrate
# sys.argv


# import sys

# print("This is the name of the program:", sys.argv[0])

# print("Argument List:", str(sys.argv))

# Python code to demonstrate the use of 'sys' module
# for command line arguments

import sys

# command line arguments are stored in the form
# of list in sys.argv
argumentList = sys.argv
print (argumentList)

# Print the name of file
print (sys.argv[0])

# Print the first argument after the name of file
# print (sys.argv[1])

from math import factorial
  
print (factorial(int(sys.argv[1])))

