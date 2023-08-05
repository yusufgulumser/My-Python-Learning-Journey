class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius=radius

    #methods
    def calcPerimeter(self):
        return 2 * self.pi + self.radius
    def calcArea(self):
        return self.pi * (self.radius**2)
    
c1= Circle() # radius=1
c2= Circle(5) # radius=5 

print(f'Perimeter is {c1.calcPerimeter()}, Area is {c1.calcArea()}')
