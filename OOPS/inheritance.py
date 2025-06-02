class Animal:

    def __init__(self,name):
        self.name = name
    
class Dog(Animal):

    def __init__(self, name,color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} speak Woof! with color {self.color}")

class Cat(Animal):

    def hi(self):
        print("Hi")


d = Dog('abhi',color='Red')
d.speak()
c = Cat('abhi2')
c.hi()
        