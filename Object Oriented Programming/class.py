#class
class Person:
    #class attributes
    address='no information'
    #constructor
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year=year

    #methods

#object(instance)
p1=Person('ali',1990)

#updating
p1.name='ahmet'
p1.address='Texas'

#accesing object attributes
print(f'p1: name: {p1.name} year: {p1.year}')