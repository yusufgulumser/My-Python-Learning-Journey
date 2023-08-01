# RANGE
for item in range(2,10):        
    print(item)
#range(a,b,c) a:start b:end c:step size
for item in range(50,100,20):   
    print(item)
# making a list with range 
print(list(range(5,100,10)))

# ENUMERATE
# Enumerating characters in a string with index and letter values
greeting='Hello'
for index,letter in enumerate(greeting):
    print(f'index:{index} letter:{letter}')
# Enumerating characters in a string and printing Tuples of (Index, Letter)
for item in enumerate('greeting'):
    print(item)

#ZIP
# Pairing elements from two lists
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
print(list(zip(list1,list2)))
