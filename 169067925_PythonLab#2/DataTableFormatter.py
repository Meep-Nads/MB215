# Activity 4: Data Table Formatter | Write a program to output a formatted table. 
# Ask for several pieces of data from the user
# Data 1
Company1 = float(input('What is the Revenue for Company 1?'))

# Data 2
Company2 = float(input('What is the Revenue for Company 2?'))

# Data 3
Company3 = float(input('What is the Revenue for Company 3?'))

# Data 4
Company4 = float(input('What is the Revenue for Company 4?'))

# Data 5
Company5 = float(input('What is the Revenue for Company 5?'))

# align them in a clean, readable format.
print(f'{'Industry Revenue':^28}')
print(f'Company 1  ${Company1:>14,.2f}')
print(f'Company 2  ${Company2:>14,.2f}')
print(f'Company 3  ${Company1:>14,.2f}')
print(f'Company 4  ${Company4:>14,.2f}')
print(f'Company 5  ${Company5:>14,.2f}')