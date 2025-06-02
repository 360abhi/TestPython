class Parent:

    def method(self):
        print("This is the parents method")

class Child(Parent):

    def method(self):
        print("This is the child method")
        super().method()

p = Parent()
p.method()

c = Child()
c.method()