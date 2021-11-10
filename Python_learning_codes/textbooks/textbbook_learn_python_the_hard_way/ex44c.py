class Parent:
    def altered(self):
        print("PARENT  altered ")
        
class Child(Parent):
    def altered(self):
        print('child, before parent altered()')
        super(Child, self).altered()
        print("child, after parent altered()")
        
dad = Parent()
son = Child()
dad.altered()
son.altered()