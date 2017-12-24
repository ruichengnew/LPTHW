## Animal is-a object (yes, sort of confusing) loot at the extra credit
class Animal(object):
    pass

## Dog is-a Amnimal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a attribute name
        self.name = name

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has-a a name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ##Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## employee is-a person, and person has-a name
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

##
mary.pet = satan

##
frank = Employee("Frank", 120000)

##
frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

##
harry = Halibut()

print(rover.name)
