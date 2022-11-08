# name: Justin Dang
# Student ID: 1148267
# Homework 2, PS1
# Randomly generats a two-digit number and prompts the user to enter a single
#two-digit number, and determines wether the user wins according to the certian rules

#variables along with an imported function
import random
USERINPUT = 49
GAME = True
print('Welcome to the Lottery!')

while GAME:
    #input
    USERINPUT = int(input('Please enter a single two-digit number or enter 0 to'
                          ' quit.'))
#generates lottery number and seperates the user and the lottery number into
#single digits
    COMPUTER = random.randint(10,99)
    COMPUTER1 = COMPUTER%10
    COMPUTER10 = int(COMPUTER/10)
    USERINPUT1 = USERINPUT%10
    USERINPUT10 = int(USERINPUT/10)
#if statements that set up conditions for winning and losing
    if USERINPUT1 == COMPUTER1:
        if USERINPUT10 == COMPUTER10:
            print('Congratulations! You guessed the exact number which was', USERINPUT,
                  'You won $10,000!')
    elif USERINPUT1 == COMPUTER1 or USERINPUT1 == COMPUTER10:
        if USERINPUT10 == COMPUTER1 or USERINPUT10 == COMPUTER10:
            print('So close! You guessed the right digits but in the wrong order!'
                  'you guessed', USERINPUT,'and the lottery number was', COMPUTER,
                  ', you won $3,000')
    if USERINPUT1 == COMPUTER1 or USERINPUT1 == COMPUTER10:
        print('You only guessed one digit. The lottery number was', COMPUTER,
              ' and you guessed',USERINPUT,', you won $1,000') 
    elif USERINPUT10 == COMPUTER1 or USERINPUT10 == COMPUTER10:
        print('You only guessed one digit. The lottery number was', COMPUTER,
              ' and you guessed',USERINPUT,', you won $1,000')
#ends the loop
    if USERINPUT == 0:
            print('Goodbye!')
            GAME = False
    else:
        print('You failed to guess the lottery number which was', COMPUTER)

## Output with 5 test cases
##
## Test Case 1.
##
##Welcome to the Lottery!
##Please enter a single two-digit number or enter 0 to quit.23
##You failed to guess the lottery number which was 90
##Please enter a single two-digit number or enter 0 to quit.43
##You failed to guess the lottery number which was 58
##Please enter a single two-digit number or enter 0 to quit.23
##You only guessed one digit. The lottery number was 72  and you guessed 23 , you won $1,000
##You failed to guess the lottery number which was 72
##4Please enter a single two-digit number or enter 0 to quit.3
##So close! You guessed the right digits but in the wrong order!you guessed 3 and the lottery number was 30 , you won $3,000
##You only guessed one digit. The lottery number was 30  and you guessed 3 , you won $1,000
##You failed to guess the lottery number which was 30
##2Please enter a single two-digit number or enter 0 to quit.3
##You only guessed one digit. The lottery number was 35  and you guessed 3 , you won $1,000
##You failed to guess the lottery number which was 35
##Please enter a single two-digit number or enter 0 to quit.43
##You failed to guess the lottery number which was 82
##Please enter a single two-digit number or enter 0 to quit.23
##You failed to guess the lottery number which was 74
##Please enter a single two-digit number or enter 0 to quit.0
##Goodbye!

## Test Case 2.
##
##Welcome to the Lottery!
##Please enter a single two-digit number or enter 0 to quit.0
##Goodbye!

## Test Case 3.
##
##Welcome to the Lottery!
##Please enter a single two-digit number or enter 0 to quit.10
##You failed to guess the lottery number which was 26
##Please enter a single two-digit number or enter 0 to quit.21
##You only guessed one digit. The lottery number was 32  and you guessed 21 , you won $1,000
##You failed to guess the lottery number which was 32
##Please enter a single two-digit number or enter 0 to quit.92
##You only guessed one digit. The lottery number was 89  and you guessed 92 , you won $1,000
##You failed to guess the lottery number which was 89
##Please enter a single two-digit number or enter 0 to quit.83
##You only guessed one digit. The lottery number was 36  and you guessed 83 , you won $1,000
##You failed to guess the lottery number which was 36
##Please enter a single two-digit number or enter 0 to quit.74
##You only guessed one digit. The lottery number was 48  and you guessed 74 , you won $1,000
##You failed to guess the lottery number which was 48
##Please enter a single two-digit number or enter 0 to quit.65
##Congratulations! You guessed the exact number which was 65 You won $10,000!
##You only guessed one digit. The lottery number was 65  and you guessed 65 , you won $1,000
##You failed to guess the lottery number which was 65
##Please enter a single two-digit number or enter 0 to quit.0
##Goodbye!

## Test Case 4.
##
##Welcome to the Lottery!
##Please enter a single two-digit number or enter 0 to quit.23
##You only guessed one digit. The lottery number was 92  and you guessed 23 , you won $1,000
##You failed to guess the lottery number which was 92
##Please enter a single two-digit number or enter 0 to quit.45
##You failed to guess the lottery number which was 29
##Please enter a single two-digit number or enter 0 to quit.67
##You failed to guess the lottery number which was 42
##Please enter a single two-digit number or enter 0 to quit.89
##You failed to guess the lottery number which was 61
##Please enter a single two-digit number or enter 0 to quit.0
##You only guessed one digit. The lottery number was 70  and you guessed 0 , you won $1,000
##Goodbye!

## Test Case 5.
##
##Welcome to the Lottery!
##Please enter a single two-digit number or enter 0 to quit.12
##You failed to guess the lottery number which was 98
##Please enter a single two-digit number or enter 0 to quit.0
##You only guessed one digit. The lottery number was 20  and you guessed 0 , you won $1,000
##Goodbye!
