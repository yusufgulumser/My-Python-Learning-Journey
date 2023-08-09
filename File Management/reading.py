try:
    file=open('newFile.txt','r')
    print(file)
except FileNotFoundError:
    print('file not found')
finally:
    print('file closed')
    file.close()

##### read() function
file=open('newFile.txt','r')
content1=file.read()
print('Content 1')
print(content1)
file.close

##
file=open('newFile.txt','r')
content1=file.read(3)            #reads the first 3 characters
print(content1)
content2=file.read(4)            #continues reading after the first 3 characters
print(content2)
file.close()

##### readline() function
file=open('newFile.txt','r')
print(file.readline())      #reads first line
print(file.readline())      #reads second line


######### Traversing
with open('newFile.txt','r') as file:        #it closes the file after code ends. No need to write file.close()
    content=file.read(10)
    print(content)
    file.seek(10)    # Prints from the 10th position onwards.
    print(file.tell())  #Prints the cursor's location
