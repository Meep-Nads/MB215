# Activity 6: Performing Calculations

# Accept two float numbers from user (a & b).
a = float(input('Enter value for a'))
b = float(input('Enter value for b'))

# Addition: Add a and b.
Addition = a + b
print(f'The sum is:{Addition}')

# Subtraction: Subtract b from a.
Subtraction = a - b 
print(f'The difference is:{Subtraction}')

# Multiplication: Multiply a by b.
Multiplication = a * b 
print(f'The product is:{Multiplication}')

# Division: Divide a by b.
if b == 0:
    print('Cannot divide by 0')
else:
    Division = a / b
    print(f'The quotient is:{Division}')

# Integer Division: Perform integer division of a by b.
if b == 0:
    print('Cannot divide by 0')
else:
    IntDivision = a // b
    print(f'The quotient is:{IntDivision}')

# Remainder: Find the remainder when a is divided by b.
if b == 0:
    print('Cannot divide by 0')
else:
    Remainder = a % b
    print(f'The quotient is:{Remainder}')

# Exponent: Calculate a raised to the power of b.
Exponent = a ** b
print(f'The power is:{Exponent}')
