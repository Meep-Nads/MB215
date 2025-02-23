import random

# Activity 2: Temperature Converter
def convert_temperature(temp, unit):
    
    #Convert Fahrenheit to Celsius if unit is f
    if unit == 'F':

        #return temperature in Celsius ('C) rounded to 2 decimals
        return f"{round(temp - 32 * 5/9,2)}'C"
    
    #Convert Celsius to Fahrenheit if unit is C
    elif unit == 'C':

        #return temperature in Fahrenheit ('F) rounded to 2 decimals
        return f"{round((temp * 9/5) + 32,2)}'F"

#Input for Temperature
temp = int(input("Enter temperature: "))

#Input for Unit F or C for Fahrenheit or Celsius
unit = input("Enter unit 'F' for Farhrenheit and 'C' for Celsius: ")

#Print What is being converting and Conversion result
print(f"A temperature of {temp}'{unit} is {convert_temperature(temp, unit)}")