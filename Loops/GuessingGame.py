#Try to guess a randomly generated number between 1 and 100 using 'up' or 'down' hints.
#Find the random module on the internet.
#Score the game out of 100 and deduct 20 points for each wrong guess.


import random
number=random.randint(1,10)
attempt=5
counter=0
while attempt>0:
    attempt-=1
    counter+=1
    guess=int(input('your guess: '))

    if number==guess:
        print(f'congrats you guessed correct in the {counter}th attempt. Your grade is {100-(20)*(counter-1)}')
        break
    elif number>guess:
        print('up')
    else:
        print('down')
    
    if attempt==0:
        print(f'you have no attempt left. The number is {number}')



