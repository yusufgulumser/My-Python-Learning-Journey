class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def whoAmI(self):
        print('I am a person')

class Student(Person):                            #Person class is inherited by the Student class.
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

p1= Person('Yusuf', 'Messi')
s1= Student('Jon','Snow')
print(p1.firstname +' '+ p1.lastname)
print(s1.firstname +' '+ s1.lastname)             

p1.whoAmI()
s1.whoAmI()               # Student class doesnt have whoAmI but it inherited from Person class
# Adding student number to Student class
class Student(Person):                            #Person class is inherited by the Student class.
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentnumber=number

s1= Student('Jon','Snow',1881)
print(s1.firstname +' '+ s1.lastname +' '+ str(s1.studentnumber)) 