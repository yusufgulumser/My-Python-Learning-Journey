#break
name=' Yusuf Gulumser'
for letter in name:
    if letter =='u':
        break     # ignores every letter after first u
    print(letter)
#continue
name=' Yusuf Gulumser'
for letter in name:
    if letter =='u':
        continue   #ignores u and prints other letters
    print(letter)

# printing numbers in a loop until reaching a break condition
x=0
while x<5:
    if x==2:
        break
    print(x)
    x+=1

# Printing numbers in a loop with continue skipping a specific value
x=0
while x<5:
    x+=1
    if x==2:
        continue
    print(x)
    
    