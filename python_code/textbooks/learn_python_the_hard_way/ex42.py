## animal is-a object (yes, sort of confusing) look at the example
class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
class Person(object):
    def __init__(self, name):
        self.name = name
        
        self.pet = None
        
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
        
class Fish(object):
    pass 

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

santan = Cat("santan")

mary = Person("Mary")

mary.pet = santan
frank = Employee("Frank", 12_000)
frank.pet = rover
flipper = Fish()
course = Salmon()

harry = Halibut()