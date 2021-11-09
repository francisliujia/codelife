ten_things = "apples Orange cows telephone light sugar"
print("Wait there are not 10 things in that list. Let's fox it")
stuff= ten_things.split()
more_stuff = ['day', 'night', 'sea', 'love', 'flower',
              'names', 'air', 'airplane', 'floor', 'master']
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")
    
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa ! fancy
print(stuff.pop())
print(''.join(stuff)) # what cool
print('£'.join(stuff[3:5])) # super stellar