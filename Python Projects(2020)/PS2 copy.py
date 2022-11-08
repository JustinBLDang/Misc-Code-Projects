# name: Justin Dang
# Student ID: 1148267
# Homework 2, PS2
# Takes an infinite amount of user inputs until user decides they are done,
# then displays name of stock, amount paid for stock, amount of commission
# user paid, amount stock was sold for, amount of commission user paid broker,
# and amount of money user has left when stock is sold along with money given to
# broker while showing profit/loss using the user input.

#Variable
DATA = True
#takes userinput and calculates values 
while DATA:
    NAME = str(input('\nEnter the name of the stock:'))
    NMBR = int(input('Enter the number of shares bought:'))
    PRICE = float(input('Enter the purchase price of the stocks:'))
    SPRICE = float(input('Enter the selling price of the stocks:'))
    COMMISSION = float(input('Enter the broker\'s commission:'))

    PAID = NMBR * PRICE
    CPAID = PAID * COMMISSION
    SOLD = NMBR * SPRICE
    SCOMMISSION = SOLD * COMMISSION
    PROFIT = (SOLD + SCOMMISSION) - (PAID + CPAID)
# outputs new values
    print('\n\nStock name:', NAME)
    print('\nAmount paid for the stock:', format(PAID, ',.2f'))
    print('Commission paid on purchase:', format(CPAID, ',.2f'))
    print('Amount the stock sold for:', format(SOLD, ',.2f'))
    print('Commission paid on the sale:', format(SCOMMISSION, ',.2f'))
#prints out different message depending on if there is a profit/loss
    if PROFIT < 0:
        print('You lost', format(PROFIT, ',.2f'))
    else:
        print('You profited', format(PROFIT, ',.2f'))
#asks user if they wish to continue 
    USERINPUT = str(input('\nDo you wish to enter more?(Type no to end or enter'
                          ' anything else to continue)'))
    if USERINPUT == "no" or USERINPUT == "No" or USERINPUT == "NO" or USERINPUT == "nO":
        print('See you next time!')
        DATA = False

## Output with 5 test cases
##
##
## Test Case 1.
##
##Enter the name of the stock:Diapers for adults
##Enter the number of shares bought:500000
##Enter the purchase price of the stocks:12
##Enter the selling price of the stocks:13
##Enter the broker's commission:.05
##
##
##Stock name: Diapers for adults
##
##Amount paid for the stock: 6,000,000.00
##Commission paid on purchase: 300,000.00
##Amount the stock sold for: 6,500,000.00
##Commission paid on the sale: 325,000.00
##You profited 525,000.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)
##
##Enter the name of the stock:Diapers for children
##Enter the number of shares bought:91283901283
##Enter the purchase price of the stocks:120
#Enter the selling price of the stocks:128
##Enter the broker's commission:.12
##
##
##Stock name: Diapers for children
##
##Amount paid for the stock: 10,954,068,153,960.00
##Commission paid on purchase: 1,314,488,178,475.20
##Amount the stock sold for: 11,684,339,364,224.00
##Commission paid on the sale: 1,402,120,723,706.88
##You profited 817,903,755,495.68
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)no
##See you next time!

## Test Case 2.
##
##
##Enter the name of the stock:yup yup
##Enter the number of shares bought:1
##Enter the purchase price of the stocks:1
##Enter the selling price of the stocks:1
##Enter the broker's commission:1
##
##
##Stock name: yup yup
##
##Amount paid for the stock: 1.00
##Commission paid on purchase: 1.00
##Amount the stock sold for: 1.00
##Commission paid on the sale: 1.00
##You profited 0.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)no
##See you next time!
        
## Test Case 3.
##
##
##Enter the name of the stock:cat
##Enter the number of shares bought:10
##Enter the purchase price of the stocks:10
##Enter the selling price of the stocks:12
##Enter the broker's commission:.04
##
##
##Stock name: cat
##
##Amount paid for the stock: 100.00
##Commission paid on purchase: 4.00
##Amount the stock sold for: 120.00
##Commission paid on the sale: 4.80
##You profited 20.80
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)
##
##Enter the name of the stock:dogs
##Enter the number of shares bought:20
##Enter the purchase price of the stocks:12
##Enter the selling price of the stocks:13
##Enter the broker's commission:.90
##
##
##Stock name: dogs
##
##Amount paid for the stock: 240.00
##Commission paid on purchase: 216.00
##Amount the stock sold for: 260.00
##Commission paid on the sale: 234.00
##You profited 38.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)
##
##Enter the name of the stock:bird
##Enter the number of shares bought:12304
##Enter the purchase price of the stocks:12
##Enter the selling price of the stocks:115
##Enter the broker's commission:.01
##
##
##Stock name: bird
##
##Amount paid for the stock: 147,648.00
##Commission paid on purchase: 1,476.48
##Amount the stock sold for: 1,414,960.00
##Commission paid on the sale: 14,149.60
##You profited 1,279,985.12
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)no
##See you next time!

## Test Case 4.
##
##
##Enter the name of the stock:pets
##Enter the number of shares bought:12879467182673
##Enter the purchase price of the stocks:123
##Enter the selling price of the stocks:189
##Enter the broker's commission:0
##
##
##Stock name: pets
##
##Amount paid for the stock: 1,584,174,463,468,779.00
##Commission paid on purchase: 0.00
##Amount the stock sold for: 2,434,219,297,525,197.00
##Commission paid on the sale: 0.00
##You profited 850,044,834,056,418.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)
##
##Enter the name of the stock:no pets
##Enter the number of shares bought:12938
##Enter the purchase price of the stocks:312
##Enter the selling price of the stocks:123
##Enter the broker's commission:.90
##
##
##Stock name: no pets
##
##Amount paid for the stock: 4,036,656.00
##Commission paid on purchase: 3,632,990.40
##Amount the stock sold for: 1,591,374.00
##Commission paid on the sale: 1,432,236.60
##You lost -4,646,035.80
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)no
##See you next time!

## Test Case 5.
##
##
##Enter the name of the stock:one
##Enter the number of shares bought:1
##Enter the purchase price of the stocks:1
##Enter the selling price of the stocks:1
##Enter the broker's commission:1
##
##
##Stock name: one
##
##Amount paid for the stock: 1.00
##Commission paid on purchase: 1.00
##Amount the stock sold for: 1.00
##Commission paid on the sale: 1.00
##You profited 0.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)
##
##Enter the name of the stock:two
##Enter the number of shares bought:2
##Enter the purchase price of the stocks:2
##Enter the selling price of the stocks:2
##Enter the broker's commission:2
##
##
##Stock name: two
##
##Amount paid for the stock: 4.00
##Commission paid on purchase: 8.00
##Amount the stock sold for: 4.00
##Commission paid on the sale: 8.00
##You profited 0.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)
##
##Enter the name of the stock:three
##Enter the number of shares bought:3
##Enter the purchase price of the stocks:3
##Enter the selling price of the stocks:3
##Enter the broker's commission:3
##
##
##Stock name: three
##
##Amount paid for the stock: 9.00
##Commission paid on purchase: 27.00
##Amount the stock sold for: 9.00
##Commission paid on the sale: 27.00
##You profited 0.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)
##
##Enter the name of the stock:four
##Enter the number of shares bought:4
##Enter the purchase price of the stocks:4
##Enter the selling price of the stocks:4
##Enter the broker's commission:4
##
##
##Stock name: four
##
##Amount paid for the stock: 16.00
##Commission paid on purchase: 64.00
##Amount the stock sold for: 16.00
##Commission paid on the sale: 64.00
##You profited 0.00
##
##Do you wish to enter more?(Type no to end or enter anything else to continue)NO
##See you next time!
