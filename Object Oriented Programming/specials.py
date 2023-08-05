mylist=[1,2,3]           #list class
mystring='my string'     #str class
class Movie():           #__main__.Movie class
    pass 
m=Movie()
print(len(mylist))          #len:3
print(len(mystring))        #len:9
print(len(m))               #has no len
##############################################################
class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.duration=duration
        self.director=director
    def __len__(self):
        return self.duration
m=Movie('Movie title','Movie director',120)
print(len(m))                                 # m has len now

# DELETING AN OBJECT
  

del(m)
print(m)           #there is no m object now

#Notify the user that it has been deleted 

def __del__(self):
    print('movie has been deleted')


#https://www.informit.com/articles/article.aspx?p=453682&seqNum=6 for more special methods in python