list=[1,2,3,4,5]
iterator=iter(list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

########### 
list=[1,2,3,4,5]
iterator=iter(list)

while True:
    try:
        element=next(iterator)
        print(element)
    except StopIteration:      #it will raise error after 6th element
        break
