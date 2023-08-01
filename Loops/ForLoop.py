# to iterate through the "numbers" list and print each element on a new line.
numbers= [1,2,3,4,5,]
for num in numbers:
  print (num)
# for writing 5 times hello
numbers= [1,2,3,4,5,]
for num in numbers:
  print ('hello')
# prints "my name is {name}" for each name in the "names" list
names=['yusuf', 'gulumser', 'kadir']
for name in names:
  print (f'my name is {name}')
# prints the two values (a, b) from each tuple on separate lines.
tuple=[(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
  print(a,b)
# prints each key on separate lines.
d={'k1':1,'k2':2,'k3':3}  #dictionary
for item in d:
   print(item)
# prints each key-value pair as a tuple on separate lines.
d={'k1':1,'k2':2,'k3':3}
for item in d.items():
  print(item)
# prints each key-value pair on separate line
d={'k1':1,'k2':2,'k3':3}
for key,value in d.items():
  print(key,value)