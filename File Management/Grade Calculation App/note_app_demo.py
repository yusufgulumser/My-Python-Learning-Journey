# Ask for the user's name and save this information to a file.
# Retrieve the averages from this file and display the letter grades (AA, AB, BB) of the grades.
def calc_notes(line):
    line=line[:-1]
    list=line.split(':')       #splits after ':'
    studentName= list[0]
    notes= list[1].split(',')

    note1=int(notes[0])
    note2=int(notes[1])
    note3=int(notes[2])

    avarage=(note1+note2+note3)/3

    if avarage>=90 and avarage<=100:
        letter= 'AA'
    elif avarage>=85 and avarage<=89:
        letter= 'BA'
    elif avarage>=80 and avarage<=84:
        letter= 'BB'
    elif avarage>=75 and avarage<=79:
        letter= 'BC'
    elif avarage>=70 and avarage<=74:
        letter= 'CC'
    elif avarage>=65 and avarage<=69:
        letter= 'DC'
    elif avarage>=60 and avarage<=64:
        letter= 'DD'
    elif avarage>=50 and avarage<=59:
        letter= 'DF'
    else:
        letter= 'FF'

    return studentName+ ':' +letter + '\n'

    

def read_notes():
    with open('exam_notes.txt','r') as file:
        for line in file:
            print(calc_notes(line))
def enter_note():
    name=input('your name: ')
    surname=input('your surname: ')
    note1=input('note1: ')
    note2=input('note2: ')
    note3=input('note3: ')

    with open('exam_notes.txt','a') as file:
        file.write(name+' '+surname+ ':'+note1+','+note2+','+note3+'\n')


def save_note():
    with open('exam_notes.txt','r') as file:
        list=[]
        for i in file:
            list.append(calc_notes(i))
        
        with open('results.txt','w') as file2:
            for i in list:
                file2.write(i)

while True:
    process=input('1-read notes\n2-enter note\n3-save note\n4 exit\n')
    if process=='1':
        read_notes()
    elif process=='2':
        enter_note()
    elif process=='3':
        save_note()
    else:
        break
