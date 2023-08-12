import os
result=os.name   # prints the operating system(nt for windows)
result=os.getcwd()   # prints the file name
print(result)

#### Changing the directories
os.chdir('C:\\')              
os.chdir('..')                # Moves to the parent directory.

#### Creating new directories
os.mkdir('newdirectory')      # creates a new directory under the current file
os.makedirs('newdirectoryy/newfolder')   # Creating a new folder within a folder
os.rename('newdirectory','changing')      # changing the name of directory
os.rmdir('newdirectory')               # removing a directory


#### Listing
os.listdir()           # Shows the active folders within the directory.
for folder in os.listdir():
    if folder.endswith('.py'):         # Shows only the files ending with .py.
        print(folder) 



#### Displaying File Creation Date using Python's datetime and os.stat
import datetime
result=os.stat('date.py')
result=datetime.datetime.fromtimestamp(result.st_ctime)    #creation date
print(result)



#### Running an application on the computer using 'os'
os.system('notepad.exe')



#### PATH
result= os.path.abspath('_os.py')    #shows the exact location of the folder
result= os.path.dirname(result)      # shows the directory
print(result)



