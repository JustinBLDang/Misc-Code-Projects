SCORE = 0
CSCORE = 0
import random
print('Type rock, paper, or scissors')
#rock is 0
#paper is 1
#scissors is 2
while(SCORE<=2 & CSCORE<=2):
    print('Type [0]rock, [1]paper, or [2]scissors')
    for x in range(3):
        COMPUTER = random.randint(0,2)
    USERINPUT = int(input('\nEnter here:'))
    if(USERINPUT == COMPUTER):
        print('Tie!')
    elif(USERINPUT == 0):
        if(COMPUTER == 1):
            print('You lose! The computer played rock and you got covered!')
            CSCORE = CSCORE + 1
            SCORE = SCORE - 1
        else:
            print('You Win! The computer played scissors and you smashed it!')
            SCORE = SCORE + 1
            CSCORE = CSCORE - 1
    elif(USERINPUT == 1):
        if(COMPUTER == 2):
            print('You lose! The computer played scissors and you got cut up!')
            CSCORE = CSCORE + 1
            SCORE = SCORE - 1
        else:
            print('You win! The computer played rock and you suffocated him with paper!')
            SCORE = SCORE + 1
            CSCORE = CSCORE - 1
    elif(USERINPUT == 2):
        if(COMPUTER == 0):
            print('You lose! The computer played rock and you got smashed!')
            CSCORE = CSCORE + 1
            SCORE = SCORE - 1
        else:
            print('You win! The computer played paper... and you SCHLICED him in half!')
            SCORE = SCORE + 1
            CSCORE = CSCORE - 1
    else:
        print('This program only takes 0, 1, 2 as an answer.')
    if(SCORE>2):
        print('YOU BEAT THE COMPUTER WOOOOOOO!')
    elif(CSCORE>2):
        print('You lost! :(')
        

