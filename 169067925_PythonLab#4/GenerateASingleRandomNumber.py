# Activity 3: Generate a Single Random Number

import random
def generate_random_number(min_val, max_val):

    #Generate random number in given range
    num = random.randint(min_val,max_val)
    return num

#Input for minimum value in range
min_val = int(input("Enter Minimum Value: "))

#Input for maximum value in range
max_val = int(input("Enter Maximum Value: "))

#print the random number generated
print(f'Your random value is: {generate_random_number(max_val,max_val)}')
