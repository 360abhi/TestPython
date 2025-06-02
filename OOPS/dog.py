class Dog:

    species = 'Canaries'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof"
    

d1 = Dog('Abhishek',34)
d2 = Dog('Chhawari',88)

print(d1.bark())
print(d2.name)
print(d2.species)

Dog.species = 'Modified'
print(d2.species)
        