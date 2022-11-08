# name: Justin Dang
# Student ID: 1148267
# Homework 2, PS4
# Calculates taxable income for both the new and old tax bracket

#Variables
TAXES = True
while TAXES:
#input
    TAX = int(input('\nEnter income as an integer with no commas:'))

#calculations
    NTAX = TAX
    TAX1 = TAX
#ends the loop
    if TAX < 0:
        break
        
    if TAX < 9526:
        FTAX = TAX * .10

    elif TAX > 9525 and TAX < 38701:
        TAX -= 9525
        TAX = TAX * .12
        FTAX = float(952.5 + TAX)

    if TAX > 38700 and TAX < 82501:
        TAX -= 38700
        TAX = TAX * .22
        FTAX = float(4453.38 + TAX)

    elif TAX > 82500 and TAX < 157501:
        TAX -= 82500
        TAX = TAX * .24
        FTAX = float(14089.16 + TAX)

    if TAX > 157500 and TAX < 200001:
        TAX -= 157500
        TAX = TAX * .32
        FTAX = float(32088.92 + TAX)

    elif TAX > 200000 and TAX < 500001:
        TAX -= 200000
        TAX = TAX * .35
        FTAX = float(45688.6 + TAX)

    if TAX > 500000:
        TAX -= 500000
        TAX = TAX * .37
        FTAX = float(150688.25 + TAX)







    if NTAX < 9326:
        FTAX1 = TAX * .10

    elif NTAX > 9325 and NTAX < 37951:
        NTAX -= 9325
        NTAX = NTAX * .15
        FTAX1 = float(932.5 + NTAX)

    if NTAX > 37950 and NTAX < 91901:
        NTAX -= 37950
        NTAX = NTAX * .25
        FTAX1 = float(5226.1 + NTAX)

    elif NTAX > 91900 and NTAX < 191651:
        NTAX -= 91900
        NTAX = NTAX * .28
        FTAX1 = float(18713.35 + NTAX)

    if NTAX > 191650 and NTAX < 416701:
        NTAX -= 191650
        NTAX = NTAX * .33
        FTAX1 = float(46643.07 + NTAX)

    elif NTAX > 416700 and NTAX < 418401:
        NTAX -= 416700
        NTAX = NTAX * .35
        FTAX1 = float(120909.24 + NTAX)

    if NTAX > 418400:
        NTAX -= 418400
        NTAX = NTAX * .396
        FTAX1 = float(121503.89 + NTAX)

    DIFFERENCE = FTAX - FTAX1
    if DIFFERENCE < 0:
        DIFFERENCE1 = DIFFERENCE * -1
        PERCENT = DIFFERENCE1 / FTAX1
        PERCENT = PERCENT * 100
    elif DIFFERENCE == 0:
        PERCENT = 0
    

# prints output in format
    print('Income:', TAX1)
    print('2017 tax:', format(FTAX1, ',.2f'))
    print('2018 tax:', format(FTAX, ',.2f'))
    print('Difference:', format(DIFFERENCE, ',.2f'))
    print('Difference (percent):', format(PERCENT, ',.2f'))

## Output with 5 test cases
##
## Test Case 1.
##
##Enter income as an integer with no commas:40000
##Income: 40000
##2017 tax: 5,738.60
##2018 tax: 4,739.38
##Difference: -999.22
##Difference (percent): 17.41
##
##Enter income as an integer with no commas:10000
##Income: 10000
##2017 tax: 1,033.75
##2018 tax: 1,009.50
##Difference: -24.25
##Difference (percent): 2.35
##
##Enter income as an integer with no commas:10000
##Income: 10000
##2017 tax: 1,033.75
##2018 tax: 1,009.50
##Difference: -24.25
##Difference (percent): 2.35
##
##Enter income as an integer with no commas:-1

## Test Case 2.
##
##Enter income as an integer with no commas:-1

## Test Case 3.
##
##Enter income as an integer with no commas:123974
##Income: 123974
##2017 tax: 27,694.07
##2018 tax: 24,042.92
##Difference: -3,651.15
##Difference (percent): 13.18
##
##Enter income as an integer with no commas:21432134
##Income: 21432134
##2017 tax: 8,442,942.55
##2018 tax: 7,895,577.83
##Difference: -547,364.72
##Difference (percent): 6.48
##
##Enter income as an integer with no commas:243214
##Income: 243214
##2017 tax: 63,659.19
##2018 tax: 60,813.50
##Difference: -2,845.69
##Difference (percent): 4.47
##
##Enter income as an integer with no commas:1234231
##Income: 1234231
##2017 tax: 444,572.97
##2018 tax: 422,353.72
##Difference: -22,219.25
##Difference (percent): 5.00
##
##Enter income as an integer with no commas:-1

## Test Case 4.
##
##Enter income as an integer with no commas:1
##Income: 1
##2017 tax: 0.10
##2018 tax: 0.10
##Difference: 0.00
##Difference (percent): 0.00
##
##Enter income as an integer with no commas:123
##Income: 123
##2017 tax: 12.30
##2018 tax: 12.30
##Difference: 0.00
##Difference (percent): 0.00
##
##Enter income as an integer with no commas:432
##Income: 432
##2017 tax: 43.20
##2018 tax: 43.20
##Difference: 0.00
##Difference (percent): 0.00
##
##Enter income as an integer with no commas:321
##Income: 321
##2017 tax: 32.10
##2018 tax: 32.10
##Difference: 0.00
##Difference (percent): 0.00
##
##Enter income as an integer with no commas:-1


## Test Case 4.
##
##Enter income as an integer with no commas:781902374981723498
##Income: 781902374981723498
##2017 tax: 309,633,340,492,718,272.00
##2018 tax: 289,303,878,743,203,456.00
##Difference: -20,329,461,749,514,816.00
##Difference (percent): 6.57
##
##Enter income as an integer with no commas:-1
