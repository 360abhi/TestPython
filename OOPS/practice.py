class Shape:

    def area(self):
        raise NotImplementedError
    
class Circle(Shape):

    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14
    
class Rectange(Shape):

    def __init__(self,height,width):
        super().__init__()
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height
    

rec = Rectange(12,23)
print(rec.area())

circ = Circle(2)
print(circ.area())

shapes = [Circle(5), Rectange(4, 6)]
for shape in shapes:
    print(shape.area()) 

