import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

property_price = float(input('Enter property price in £GBP: '))
ltv = float(input('Enter the maximum LTV offered by your bank: '))

loan_amount = property_price*(ltv/100)

print("The loan amount is: = " + str(property_price*(ltv/100)))
print("The deposit amount is: = " + str(property_price*(1-(ltv/100))))

deposit = float(input('Enter amount of deposit: '))

new_ltv = (1-(deposit/property_price))*100

print("The new LTV would be of: = " + str(new_ltv) + str('%'))