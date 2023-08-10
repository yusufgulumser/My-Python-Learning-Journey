# Generators allow you to produce values one at a time instead of all at once
def cube():
    for i in range(5):
        yield i**3    #The yield used to create a generator.

for i in cube():
    print(i)