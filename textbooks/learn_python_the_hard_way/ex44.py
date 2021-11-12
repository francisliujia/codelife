class Parent:
    def override(self):
        print("parent override()")
    def implicit(self):
        print('parent implicit()')
    def altered(self):
        print('parent altered()')
        
class Child(Parent):
    def override(self):
        print('child override()')
    def altered(self):
        print('child, before parent altered()')
        super(Child, self).altered()
        print('child, after parent altered()')
        
dad  = Parent()
son = Child()

dad.override()
son.override()
dad.altered()
son.altered()



