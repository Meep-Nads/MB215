import random

# Activity 4: Investment Simulator. 

def simulate_investment(amount, years, rate_min, rate_max):
# add starting amount to total
    final_amount = amount

    # Loop for inputed amount of years
    for num in range(years):
        rate = 0

         # Determine interest rate
        rate = random.uniform(rate_min,rate_max)

         # Determine Interest and add to final amount 
        final_amount += (amount * rate)
        
    return final_amount

rate_min = -2 
rate_max = 15
# input for amount initially invested
amount = int(input('Enter Investment Amount: '))
# input for amount of years to invest
years = int(input('Enter Investmetn period in Years: '))

# Investment Simulation
final_amount = simulate_investment(amount, years, rate_min, rate_max)
print(f"Final investment value after 5 years: ${final_amount:.2f}")