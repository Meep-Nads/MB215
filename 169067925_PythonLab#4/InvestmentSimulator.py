import random

# Activity 1: Customizable Dice Simulator
import TemperatureConverter as TemperatureConverter

import CustomizableDiceSimulator

import GenerateASingleRandomNumber as GenerateASingleRandomNumber


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



# Call the above functions Demonstrate the results
if __name__ == "_main_":
    # Dice Simulation
     
    print(f'(Rolling 3 dice with 6 sides each:...{CustomizableDiceSimulator}')
    
    # Temperature Conversion
    print("Converting 100F to Celsius:", TemperatureConverter)
    #print("Converting 0C to Fahrenheit:", …………….))
    
    # Generate a Single Random Number
    #random_number = 
    #print(f"The generated random number is: {random_number}")


    # Investment Simulation
    final_amount = simulate_investment(amount, years, rate_min, rate_max)
    print(f"Final investment value after 5 years: ${final_amount:.2f}")
