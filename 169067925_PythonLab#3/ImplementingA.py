# Create a program that continuously asks the user to enter numbers. 
# These numbers are added to a running total sum. 
# The while loop should continue as long as the total sum is less than 100. 
# However, if the user enters a space (“”), the loop should break, regardless of the total sum. 
# After exiting the loop, the program should display the total sum and the count of numbers entered. 
# Here are some instructions:

# Initialize variables to store the total sum (starting at 0) and the count of numbers entered.
totalsum = range(0,100)
count = 0

# Implement a while loop that continues as long as the total sum is less than 100.
while totalsum < 100:
# Inside the loop, prompt the user to either enter a number or a space (' ') to exit.
    Deposit = input('Enter Amount to Deposit or a space to Exit:')

# If the user enters a space, break out of the loop immediately.
    if Deposit == (' '):
        break


# If the user enters a number, add it to the total sum and increment the count.
    else:
        totalsum += int(Deposit)
        count += 1

# Once the loop is exited (either the sum reaches/exceeds 100 or the user enters a space), display the total sum and the count of numbers entered.
print(int(f'Your total Balance is: {totalsum}  You have made a total of: {count} deposits'))