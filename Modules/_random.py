import random 

result=random.random()    # 0.0,0.341,......,1.0
result=int(random.uniform(10,100))  # 10,11...99,100
result=random.randint(10,100)       # 10,11,..99,100


names=['ali','yağmur','jon','burak']
result=names[random.randint(0,len(names)-1)]   # prints a random name index 0 to index 3
result=random.choice(names)                    # 'random.choice' method prints a random name index 0 to index 3
result=random.sample(names,2)                  # selects 2 random names from 'names'

print(result)