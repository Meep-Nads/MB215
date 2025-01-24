# Write a simple Python program that demonstrates the use of Boolean variables. Your program should perform the following tasks:
# Create two Boolean variables with values True and False.
# Use these variables in a series of basic logical operations (AND, OR, NOT) and print the results.
# Include an example of a conditional statement (if-else) that uses a Boolean variable.

# Step 1: Declare two Boolean variables
alive = True
dead = False

# Step 2: Demonstrate logical operatons (AND, OR, NOT)

# Logical AND
print(alive and dead)
# a = 42 and b = 0 

# Logical OR
print(alive or dead)

# Logical NOT
print(not(alive))

# Step 3: Use a Boolean variable in conditional statement
result = 'Yay your alive' if alive < dead else 'Oh no your dead'
print(result)

# Conditional statement with logical operation
result = 'Yay your not dead' if not(dead) else 'Whoop Whoop'
print(result)