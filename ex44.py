# two kinds of way to use class
# inheriance and composition

class Parent(object):

    def altered(self):
        print("Parent.implicit")

class Child(Parent):

    def alteredself):
        print("Child, before parent altered()")
        super(Child, self).altered()
        print("Child, after parent altered()")

dad = Parent()
son = Child()
dad.altered()
son.altered()
