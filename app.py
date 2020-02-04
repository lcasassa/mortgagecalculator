import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# finding out the maximum loan value according to property price
property_price = float(input('Enter property price in GBP: '))
ltv = float(input('Enter the maximum LTV offered by your bank: '))

loan_amount = property_price*(ltv/100)
min_deposit = np.round((property_price*(1-(ltv/100))), 2)

print("The loan amount would be of: = £{}".format(loan_amount))
print("At a LTV of {}%,".format(ltv) + "your minimum deposit would be of: = £{}".format(min_deposit))

# deposit according to LTV or higher
deposit = float(input('Enter amount of deposit, this can be higher to reduce your LTV and the amount of the loan: '))

new_ltv = np.round((1-(deposit/property_price))*100, 2)
deposit_percentage = np.round((deposit/property_price)*100, 2)

# check if deposit is equal or higher than the minimum; calculate respective LTV if necessary
while deposit < min_deposit: 
    print("I'm sorry, but your deposit can't be lower that {}".format(min_deposit))
    deposit = float(input('Enter a value that is equal or higher to £{} '.format(min_deposit)))
    if deposit > min_deposit:
        print("With that deposit, the LTV would be of: = {}%".format(new_ltv))
        print("And the deposit as a percentage of the value would be of: = {}%".format(deposit_percentage))
    elif deposit == min_deposit:
        print("Excellent! let's find out more about your mortgage")
        break

# calculating monthly repayments based on interest and mortgage type in years
interest = float(input('Please enter the annual interest rate for the loan: '))
mortgage_type = float(input('Enter mortgage type in years, e.g. 15 for 15 years: '))

loan_term = int(12*mortgage_type)
monthly_interest = (interest/12)
#capital recovery factor
capital_rf = (1-(1+interest/(12*100))**(-loan_term))

monthly_repayments = loan_amount*((interest/(12*100))/capital_rf)

# for calculating total interet paid
value_of_loan = (monthly_repayments*loan_term)
total_interest = value_of_loan - loan_amount

# summary of monthly payments, how many, interest to be paid
print("Your monthly repayments would be of: £{}".format(np.round(monthly_repayments, 2)))
print("You have a total of {} monthly repayments".format(loan_term) + " which add up to a total value of the loan of £{}".format(np.round(value_of_loan, 2)))
print("The total interest to be paid is of: £{}".format(np.round(total_interest, 2)))

# interest curve
interest_monthly = []
month_starting_balance = []
month_ending_balance = []

# use range to generate sequence of numbers from 1 to the last loan month
# for a in range(1, loan_term+1):
#     end_of_month = loan_amount + monthly_interest*loan_amount - monthly_repayments
