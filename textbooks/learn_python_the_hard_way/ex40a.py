import mystuff
mystuff.apple()
print(mystuff.tangerine)
    
    
# print(apple())

class MyStuff(object):
    def __init__(self):
        self.tangerine = "and now a thousand years between"
    def apple(self):
        print(" I am classy apples")
        
thing = MyStuff()
thing.apple()
print(thing.tangerine)
