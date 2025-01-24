# take a variable with distance in kilometers as input
km = float(input("Enter Distance in Kilometer: "))

# output the same distance converted to miles, round the final vale to 2 decimals
conversion = 0.621371
miles = round(km * conversion,2)

# print the final answer
print(f'That is: {miles} in miles')