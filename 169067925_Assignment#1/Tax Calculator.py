#Question 1. Tax Calculator
#Develop a program that calculates Ontario Tax based on the following formula:

#Your program should:

#1.	Prompt the user to enter their taxable income.
tax_income = int(input('Enter amount of taxable income: $'))

#2.	Display the tax amount based on the input from step 1 (referred to as the result from line 38 in the formula).
#Calculating amount of tax when taxable income is greater than 220000
if tax_income >= 220000:
    tax_rate = 0.1316
    tax_amount = ((tax_income - 220000) * tax_rate) + 21929
    print(f'Ontario tax on Taxable Amount: ${tax_amount}')
#Calculating amount of tax when taxable income is between 15,000 - 220,000
elif tax_income in range(150000,220000):
    tax_rate = 0.1216
    tax_amount = (tax_income - 150000) *tax_rate + 13417
    print(f'Ontario tax on Taxable Amount: ${tax_amount}')
#Calculating amount of tax when taxable income is between 81,847-150,000
elif tax_income in range(81847,150000):
    tax_rate = 0.1116
    tax_amount = (tax_income - 81847) * tax_rate + 5811
    print(f'Ontario tax on Taxable Amount: ${tax_amount}')
#Calculating amount of tax when taxable income is between 40,922 - 81,847
elif tax_income in range(40922,81847):
    tax_rate = 0.915
    tax_amount = (tax_income - 40922) * tax_rate + 2067
    print(f'Ontario tax on Taxable Amount: ${tax_amount}')
#Calculating amount of tax when taxable income is less than 40,922
elif tax_income <= 40922:
    tax_rate = 0.505
    tax_amount = tax_income * tax_rate
    print(f'Ontario tax on Taxable Amount: ${tax_amount}')
#If taxable income amount is invalid
else:
    print('Invalid input Taxable income amount')

#Ask the user to enter the amount of tax they have already paid.
tax_paid = int(input('Enter amount of tax paid: $'))

#Calculate and display the remaining tax balance. 
tax_amount -= tax_paid

#If the remaining tax balance is zero or negative, display a message indicating that the user is eligible for a refund.
if tax_amount <= 0:
   print(f'Tax balance is zero, you are eligible for a refund: ${tax_amount}')
#If remaining tax balance is greater than zero, display tax balance
else:
   print(f'Remaining tax balance: ${tax_amount}')

# Note: If the user is entitled to a refund, this balance will be a negative number, indicating the refund amount."
