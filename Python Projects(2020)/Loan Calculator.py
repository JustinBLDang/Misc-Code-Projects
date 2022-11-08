# name: Justin Dang
# Student ID: 1148267
# Homework 5, Problem Set 3

'''Calculates and displays a loan for buying a car'''

class Loan:
    def __init__(self, interest, years, loan, name):
        self._monthlyInterestRate = interest
        self._numberOfYears = years
        self._loanAmount = loan
        self._name = name

    def get_interest(self):
        return self._monthlyInterestRate

    def get_years(self):
        return self._numberOfYears

    def get_loan(self):
        return self._loanAmount

    def get_name(self):
        return self._name

    def set_interest(self, x):
        self._monthlyInterestRate = x

    def set_years(self, x):
        self._numberOfYears = x

    def set_loan(self, x):
        self._loanAmount = x

    def set_name(self, x):
        self._name = x

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount*monthlyInterestRate/(1 - (1/(1+monthlyInterestRate)**(numberOfYears*12)))
        return monthlyPayment
    
    def getTotalPayment(self, monthlyPay, numberOfYears):
        totalPayment = monthlyPay * numberOfYears * 12
        return totalPayment
def main():
    interest = float(input('Enter yearly interest rate:'))
    year = float(input('Enter number of years as an integer:'))
    loan = float(input('Enter loan amount:'))
    name = str(input("Enter a borrower's name:"))

    carLoan = Loan(interest, year, loan, name)
    carLoan.set_interest(interest/1200)
    carLoan.set_years(year)
    carLoan.set_loan(loan)
    carLoan.set_name(name)
    interest = carLoan.get_interest()
    year = carLoan.get_years()
    loan = carLoan.get_loan()
    name = carLoan.get_name()
    
    monthlyPay = carLoan.getMonthlyPayment(loan, interest, year)
   
    print('The loan is for', carLoan.get_name())
    print('The monthly payment is', format(monthlyPay, ',.2f'))
    print('The total payment is', format(carLoan.getTotalPayment(monthlyPay, year), ',.2f'))

    while True:
        userinput = str(input('Do you want to change the loan amount? Y for yes or enter to quit '))
        if userinput == 'y' or userinput == 'Y':
            loan = float(input('Enter new loan amount:'))

            carLoan.set_loan(loan)
            loan = carLoan.get_loan()
            monthlyPay = carLoan.getMonthlyPayment(loan, interest, year)

            print('The loan is for', carLoan.get_name())
            print('The monthly payment is', format(monthlyPay, ',.2f'))
            print('The total payment is', format(carLoan.getTotalPayment(monthlyPay, year), ',.2f'))
        else:
            break
            

###########################################################main()

#Output with test cases
##
##Test case 1.
##
##Enter yearly interest rate:2.5
##Enter number of years as an integer:5
##Enter loan amount:1000
##Enter a borrower's name:g
##The loan is for g
##The monthly payment is 17.75
##The total payment is 1,064.84
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount:5000
##The loan is for g
##The monthly payment is 88.74
##The total payment is 5,324.21
##Do you want to change the loan amount? Y for yes or enter to quit 

##Test case 2.
##
##Enter yearly interest rate:3.4
##Enter number of years as an integer:3
##Enter loan amount:5000
##Enter a borrower's name:justin
##The loan is for justin
##The monthly payment is 146.29
##The total payment is 5,266.41
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount:32
##The loan is for justin
##The monthly payment is 0.94
##The total payment is 33.71
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount:82395
##The loan is for justin
##The monthly payment is 2,410.70
##The total payment is 86,785.14
##Do you want to change the loan amount? Y for yes or enter to quit 
        
##Test case 3.
##
##Enter yearly interest rate:1
##Enter number of years as an integer:1
##Enter loan amount:1
##Enter a borrower's name:one
##The loan is for one
##The monthly payment is 0.08
##The total payment is 1.01
##Do you want to change the loan amount? Y for yes or enter to quit   

##Test case 4.
##
##Enter yearly interest rate:4.9
##Enter number of years as an integer:45
##Enter loan amount:1000
##Enter a borrower's name:uh oh
##The loan is for uh oh
##The monthly payment is 4.59
##The total payment is 2,479.61
##Do you want to change the loan amount? Y for yes or enter to quit nope

##Test case 5.
##
##Enter yearly interest rate:10
##Enter number of years as an integer:1
##Enter loan amount:10000
##Enter a borrower's name:charles
##The loan is for charles
##The monthly payment is 879.16
##The total payment is 10,549.91
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount:10
##The loan is for charles
##The monthly payment is 0.88
##The total payment is 10.55
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount:0
##The loan is for charles
##The monthly payment is 0.00
##The total payment is 0.00
##Do you want to change the loan amount? Y for yes or enter to quit 
        
# name: Justin Dang
# Student ID: 1148267
# Homework 5, Problem Set 4

'''using tkinter to create a GUI for problem set 3'''
import tkinter as tk
from functools import partial
def call_result(label_result, n1, n2, n3):
    monthlyInterestRate = (float(n1.get()) / 1200)
    numberOfYears = (float(n2.get()))
    loanAmount = (float(n3.get()))
    monthlyPay = float(loanAmount)*float(monthlyInterestRate)/(1 - (1/(1+float(monthlyInterestRate))**(float(numberOfYears)*12)))
    totalPay = monthlyPay * numberOfYears * 12
    monthlyPayment.config(text= format(monthlyPay, ',.2f'))
    totalPayment.config(text= format(totalPay, ',.2f'))
    return

#sets up labels and title of calculator
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Loan Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
labelTitle = tk.Label(root, text="Loan Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Annual Interest").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Number of Years").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Loan Amount").grid(row=3, column=0)
labelNum4 = tk.Label(root, text="Monthly Payment").grid(row=4, column=0)
labelNum5 = tk.Label(root, text="Total Payment").grid(row=5, column=0)

#sets up entry boxes to recieve user input and establishes where output is places
monthlyPayment = tk.Label(root)
monthlyPayment.grid(row=4, column=2)
totalPayment = tk.Label(root)
totalPayment.grid(row=5, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)

#sets up button
call_result = partial(call_result, monthlyPayment, number1, number2, number3)
buttonCal = tk.Button(root, text="Compute Payment", command=call_result).grid(row=6, column=2)
root.mainloop()
