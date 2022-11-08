#random door game
#picks a random door 1-3
#user plays guessing game and gets points
#if they pick ghost door they get a boo and are given their score

#2 decimal points
HIGHSCORE = 0
GAME = True
import random
for x in range(3):
    DOOR = random.randint(1,3)

print('Pick a door by typing 1,2 3')

while True:
    while GAME:
        for x in range(3):
            DOOR = random.randint(1,3)
        USERINPUT = int(input('Enter here:'))
        if(DOOR == USERINPUT):
            print('BOOOOOOOOOOOOOOO')
            print('Game Over')
            GAME = False
        elif(DOOR != USERINPUT):
            print('Nothing appears to have been behind this door...')
            print('Pick a door by typing 1,2 3')
            HIGHSCORE = HIGHSCORE + 1

    AGAIN = str(input('Type quit to end the game or press anything to play again!'))
    if AGAIN == 'quit' or AGAIN == 'Quit':
        break
    else:
        GAME = True





print('You scored', HIGHSCORE)

