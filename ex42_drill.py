class Dog(object):

    def __init__(self, name):
        self.name = name
        self.size = None

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

dog1 = Dog("dog1")
dog1.size = 3
dog2 = Dog("dog2")
dog2.size = 2
dog3 = Dog("dog3")
dog3.size = 1
frank = Employee("Frank", "120000")
print(frank.salary)
