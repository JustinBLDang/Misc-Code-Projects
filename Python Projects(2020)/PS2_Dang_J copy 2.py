# name: Justin Dang
# Student ID: 1148267
# Homework 3, Problem set 2
'''
Detects wether the string entered is a palindrome
'''
#Reverses string and checks if what the user entered was a palindrome
def isPalindrome()->(bool):
    STRING = str(input('Enter a String : '))
    for x in range(0, len(STRING)):
        if STRING[x] != STRING[-(x+1)]:
            print(STRING, 'is not a palindrome')
            break
        else:
            print(STRING, 'is a palindrome')
            break

#Determines how many times the user would like to check if a word is a palindrome
def main():
    COUNT = 1
    USERINPUT = int(input('How many words do you want to check?'))
    while COUNT <= USERINPUT:
        COUNT += 1
        isPalindrome()
        print()
    
if __name__ == '__main__':
    main()

## Output with test cases
##
## Test Case 1.
##
##How many words do you want to check?2
##Enter a String : 34
##34  is not a palindrome
##
##Enter a String : noon
##noon  is a palindrome

## Test Case 2.
##
##How many words do you want to check?2
##Enter a String : 121
##121 is a palindrome
##
##Enter a String : help
##help is not a palindrome

## Test Case 3.
##
##How many words do you want to check?5
##Enter a String : 123321
##123321 is a palindrome
##
##Enter a String : noon
##noon is a palindrome
##
##Enter a String : poop
##poop is a palindrome
##
##Enter a String : palindrome
##palindrome is not a palindrome
##
##Enter a String : dog
##dog is not a palindrome

## Test Case 4.
##
##How many words do you want to check?3
##Enter a String : three
##three is not a palindrome
##
##Enter a String : four
##four is not a palindrome
##
##Enter a String : god
##god is not a palindrome

## Test Case 5.
##
##How many words do you want to check?4
##Enter a String : follof
##follof is a palindrome
##
##Enter a String : wow
##wow is a palindrome
##
##Enter a String : meater eater
##meater eater is not a palindrome
##
##Enter a String : meateretaem
##meateretaem is a palindrome
