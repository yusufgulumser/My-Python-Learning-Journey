#The 'open()' function is used to open and create files.
#Usage: open(file_name,file_access_mode)
#File access mode: specifies the purpose for which we are opening the file.

#### w(Write): 
#Creates the file at the location.
#Deletes the file content and rewrites the file content.
file=open("newFile.txt","w")
file.write('ben yusuf')
file.close()

#### a(Append):
#If the file doesn't exist in the location, it creates the file.
file=open("newFile.txt","a")
file.write('ben yusuf')            #Appends to the file content.
file.close()

#### x(Create):
#Raises an error if the file already exists.
file=open("newFile","x")
file=open("newFile.txt""x")      #error

#### r(Read):
#Raises an error if the file doesn't exist in the location.
