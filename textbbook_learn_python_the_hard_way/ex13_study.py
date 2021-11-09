from sys import argv

# read the WYSS section for how to run this

fruit = input("what is your favorite fruit?", end='')
animal = input("What is your favorite animal? ", end='')
person = input("who is your favorite person?", end='')


like_list, fruit, animal, person = argv

print("The like list is called:", like_list)
print("Your favourite fruit is :", fruit)
print("Your favorite animal is:", animal)
print("Your favorite person is: ", person)
