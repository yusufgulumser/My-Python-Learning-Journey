import re

str='What is python? Python is the best programming language'

#re.findall
result= re.findall('python',str)  #finds and prints it
result= len(result)               #shows the count

#re.split
result= re.split(' ',str)            #splits the string 

#re.sub
result=re.sub(' ','-',str)          # replaces blanks with '-'

#re.search
result=re.search('programming',str)      #shows the location of the 'programming'. (35,46)
result=result.span()                     # prints(35,46)
result=result.start()                    # prints 35
result=result.end()                      # prints 46
result=result.group()                    # prints 'programming'
result=result.string                     # prints the 'str'




print(result)   

