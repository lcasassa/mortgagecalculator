import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

property_price = float(input('Enter property price in GBP: '))
ltv = float(input('Enter the maximum LTV offered by your bank: '))

loan_amount = property_price*(ltv/100)

print("The loan amount would be of: = £" + str(property_price*(ltv/100)))
# reduce float for the deposit to 2 decimal points
print("At a LTV of {}%, your deposit would be of: = £".format(ltv) + str(property_price*(1-(ltv/100))))

deposit = float(input('Enter amount of deposit, this can be higher to reduce your LTV and the amount of the loan: '))

new_ltv = (1-(deposit/property_price))*100
deposit_p = (deposit/property_price)*100

print("With that deposit, the LTV would be of: = {}%".format(new_ltv))
print("And the deposit as a percentage of the value would be of: = {}%".format(deposit_p))

mortgage_type = float(input('Enter mortgage type in years, e.g. 15 for 15 years: '))
loan_term = int(12*mortgage_type)