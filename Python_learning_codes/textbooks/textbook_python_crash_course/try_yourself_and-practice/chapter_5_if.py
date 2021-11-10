'''
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response as you wish.")
''

age = 17
if age >= 18:
	print("You are old enough to vote!")
	print('Have you registed to vote yet?')

else:
	print("Sorry, you are too young to vote.")
	print("\nPlease register to vote as soon as you turn 18!")

''
age = 12
if age < 4:
    print("Your admission cost is free.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40")
''

age = 80
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 60:
    price = 20
elif age >= 60:
    price = 10

print(f"Your admission cost is ${price}.")
''

requested_topplings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topplings:
	print("Adding extra mushrooms.")
if 'extra cheese' in requested_topplings:
	print("Adding extra cheese.")
print("\nFinished your pizza!")
''

requested_topplings = ['mushrooms', 'extra cheese', 'green peppers']
for requested_toppling in requested_topplings:
	if requested_toppling == 'green peppers':
		print("Sorry we are running out of " + requested_toppling.title() + "!")
    else:
    	print("Adding " + requested_toppling.title() )

print("Finished making your pizza!")  
''
requested_topplings = []
if requested_topplings:
	for requested_toppling in requested_topplings:
		print(123)
	print(1234)
else:
	print("Are you sure you want a plain pizza?")
'''

avaiable_topplings = ['mushrooms', 'olives', 'green peppers',

                      "pepperoni", 'pineaple', 'extra cheese']

requested_topplings = ['mushrooms', 'frenchf ries', 'extra cheese']
for requested_toppling in requested_topplings:
    if requested_toppling in avaiable_topplings:
        print("Adding extra" + requested_toppling + ".")
    else:
        print("Sorry, we don't have " + requested_toppling + ".")
print("\nFinished making your pizza!")
