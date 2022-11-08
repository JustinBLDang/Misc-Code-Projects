# name: Justin Dang
# Student ID: 1148267
# Homework 3, Problem set 1

'''
Allows user to enter as many stocks as they want and returns information
along with calculations
'''
#gets userinput and calculates data to allow for output depending on information given
def stocks()->(str):
    NAME = str(input('Enter the name of the stock:'))
    SHARES = float(input('Enter the number of shares bought:'))
    PPRICE = float(input('Enter the purchase price:'))
    SPRICE = float(input('Enter the selling price:'))
    COMMISSION = float(input('Enter the commission percent:'))
    
    PAID = SHARES * PPRICE
    PCOMMISSION = PAID * COMMISSION
    SOLD = SHARES * SPRICE
    SCOMMISSION = SOLD * COMMISSION
    PROFITLOSS = (PAID + PCOMMISSION) - (SOLD - SCOMMISSION)
    
    print('Stock Name:', NAME)
    print()
    print('Amount paid for stock:       ${:>10,.2f}'.format(PAID))
    print('Amount of commission paid:   ${:>10,.2f}'.format(PCOMMISSION))
    print('Amount that stock sold for:  ${:>10,.2f}'.format(SOLD))
    print('Amount of commission sold:   ${:>10,.2f}'.format(SCOMMISSION))
    print('PROFIT/LOSS:                 ${:>10,.2f}'.format(PROFITLOSS))
#initiates function and determines wether function breaks depending on user
if __name__== '__main__':
    USERINPUT = ''
    while USERINPUT != "done" and USERINPUT != "Done":
        USERINPUT = str(input('Enter anything to input stock information or type done to quit the program:'))
        if USERINPUT != "done" and USERINPUT != "Done":
            stocks()
        else:
            print('Have a nice day!')
            break

## Output with test cases
##
## Test Case 1.
##
##Enter anything to input stock information or type done to quit the program:Done
##Have a nice day!

## Test Case 2.
##
##Enter anything to input stock information or type done to quit the program:iorwnf
##Enter the name of the stock:GoodYear
##Enter the number of shares bought:1100
##Enter the purchase price:33.2
##Enter the selling price:33
##Enter the commission percent:.09
##Stock Name: GoodYear
##
##Amount paid for stock:       $ 36,520.00
##Amount of commission paid:   $  3,286.80
##Amount that stock sold for:  $ 36,300.00
##Amount of commission sold:   $  3,267.00
##PROFIT/LOSS:                 $  6,773.80
##Enter anything to input stock information or type done to quit the program:
##Enter the name of the stock:BadYear
##Enter the number of shares bought:34
##Enter the purchase price:10
##Enter the selling price:11
##Enter the commission percent:2
##Stock Name: BadYear
##
##Amount paid for stock:       $    340.00
##Amount of commission paid:   $    680.00
##Amount that stock sold for:  $    374.00
##Amount of commission sold:   $    748.00
##PROFIT/LOSS:                 $  1,394.00
##Enter anything to input stock information or type done to quit the program:done
##Have a nice day!

## Test Case 3.
##
##Enter anything to input stock information or type done to quit the program:no
##Enter the name of the stock:12345
##Enter the number of shares bought:12345
##Enter the purchase price:1234
##Enter the selling price:1.2345
##Enter the commission percent:12.345
##Stock Name: 12345
##
##Amount paid for stock:       $15,233,730.00
##Amount of commission paid:   $188,060,396.85
##Amount that stock sold for:  $ 15,239.90
##Amount of commission sold:   $188,136.60
##PROFIT/LOSS:                 $203,467,023.54
##Enter anything to input stock information or type done to quit the program:done
##Have a nice day!
                         
## Test Case 4.
##
##Enter anything to input stock information or type done to quit the program:
##Enter the name of the stock:one
##Enter the number of shares bought:1
##Enter the purchase price:1
##Enter the selling price:1
##Enter the commission percent:1
##Stock Name: one
##
##Amount paid for stock:       $      1.00
##Amount of commission paid:   $      1.00
##Amount that stock sold for:  $      1.00
##Amount of commission sold:   $      1.00
##PROFIT/LOSS:                 $      2.00
##Enter anything to input stock information or type done to quit the program:2
##Enter the name of the stock:two
##Enter the number of shares bought:2
##Enter the purchase price:2
##Enter the selling price:2
##Enter the commission percent:2
##Stock Name: two
##
##Amount paid for stock:       $      4.00
##Amount of commission paid:   $      8.00
##Amount that stock sold for:  $      4.00
##Amount of commission sold:   $      8.00
##PROFIT/LOSS:                 $     16.00
##Enter anything to input stock information or type done to quit the program:3
##Enter the name of the stock:three
##Enter the number of shares bought:3
##Enter the purchase price:3
##Enter the selling price:3
##Enter the commission percent:3
##Stock Name: three
##
##Amount paid for stock:       $      9.00
##Amount of commission paid:   $     27.00
##Amount that stock sold for:  $      9.00
##Amount of commission sold:   $     27.00
##PROFIT/LOSS:                 $     54.00
##Enter anything to input stock information or type done to quit the program:done
##Have a nice day!

## Test Case 5.
##
##Enter anything to input stock information or type done to quit the program:anything
##Enter the name of the stock:anything
##Enter the number of shares bought:3242135231
##Enter the purchase price:3215123
##Enter the selling price:32153125
##Enter the commission percent:21352135
##Stock Name: anything
##
##Amount paid for stock:       $10,423,863,550,298,412.00
##Amount of commission paid:   $222,571,741,747,550,980,407,296.00
##Amount that stock sold for:  $104,244,779,349,246,880.00
##Amount of commission sold:   $2,225,848,601,710,331,523,235,840.00
##PROFIT/LOSS:                 $2,448,420,249,636,966,749,962,240.00
##Enter anything to input stock information or type done to quit the program:done
##Have a nice day!
