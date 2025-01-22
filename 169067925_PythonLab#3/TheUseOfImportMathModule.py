# Write a Python program to calculate the volume of a cylinder 
# The program should perform the following steps:
# import the math module.
import math

# ask the user to input the diameter of the cylinder's circular end.
diameter = float(input("Enter Diameter of Cylinder's circular end in cm:"))

# ask the user to input the height of the cylinder.
height = float(input("Enter Height of Cylinder in cm:"))

# consider the initial value of pi = 3.141592 and then round it to 2 decimal places
# (:=) Walrus operator, assigns number value to variable
pi = (num :=  round(math.pi,2))

# calculate the radius of the cylinder's circular end.
radius = ( num := 2 / diameter)

# calculate the volume of the cylinder using the formula: volume = pi* radius² * height.
volume = round((num := pi * (radius ** 2) * height),2)

# output the calculated volume
# How do I make the 'cm cubed' and make look proper
print(f"The Volume of the Cylinder is: {volume}cm cubed")