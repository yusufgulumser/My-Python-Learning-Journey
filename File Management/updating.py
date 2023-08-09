with open('newFile.txt','r+') as file:     #r+ : reads and writes
    file.seek(10)
    file.write('type')                     #writes 'type' after 10th byte

with open('newFile.txt','r') as file:
    print(file.read())

##### Updating at the beginning of the page ######
with open('newFile.txt','r+') as file:
    content=file.read()
    content='melo turan\n'+content
    file.seek(0)
    file.write(content)

with open('newFile.txt','r') as file:
    print(file.read())

##### Updating in the middle of the page #####
with open('newFile.txt','r+') as file:
    list=file.readlines() 
    list.insert(1,'melih kaya\n')    #Writes 'melih kaya' after the 1st index and updates the list.
    file.seek(0)
    file.writelines(list)   

with open('newFile.txt','r') as file:
    print(file.read())         


##### Updating at the end of the page ######
with open('newFile.txt','a') as file:
    file.write('\nEmel tur')

with open('newFile.txt','r') as file:
    print(file.read()) 