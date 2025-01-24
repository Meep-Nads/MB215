# Create a Python program that demonstrates the uses of “for” loops, including nested loops, iterating with the “range()” function in various ways, and looping through strings. 
# Here is the instructions:

# Implement a for loop with ‘range()’ to iterate through and print even numbers.
# Create a nested for loop where the outer loop represents the numbers 1 to 3 and the inner loop represents a range from 1 to 10. Use these loops to print a multiplication table.
# Write a ‘for’ loop to reverse the characters of a given string and print them.
# Code template:
# Python Program for Demonstrating Different Uses of for Loops

# For loop with range to print even numbers from 2 to 20
for num in (range(2,22, + 2)):
    print(num)
    #print(f'{num:<}',end = ' ')
# Expected output:
# Even numbers from 2 to 20: 2 4 6 8 10 12 14 16 18 20

# Nested for loop to create a multiplication table for numbers 1 to 3
for outer in (1,2,3):
    for inner in range(1,11,1):
        muliply = outer * inner
        print((f'{outer} * {inner} = {muliply}'))
        
# Expected output:
# Multiplication table for numbers 1 to 3:
# 1 * 1 = 1       1 * 2 = 2       1 * 3 = 3       1 * 4 = 4       1 * 5 = 5       1 * 6 = 6       1 * 7 = 7
# 1 * 8 = 8       1 * 9 = 9       1 * 10 = 10
# 2 * 1 = 2       2 * 2 = 4       2 * 3 = 6       2 * 4 = 8       2 * 5 = 10      2 * 6 = 12      2 * 7 = 14
# 2 * 8 = 16      2 * 9 = 18      2 * 10 = 20
# 3 * 1 = 3       3 * 2 = 6       3 * 3 = 9       3 * 4 = 12      3 * 5 = 15      3 * 6 = 18      3 * 7 = 21
# 3 * 8 = 24      3 * 9 = 27      3 * 10 = 30


# For loop to reverse a string. Note : Use ‘Reserved’ Key word
for letter in reversed('Reserved'):
    print(letter, end= ' ')
    
# Expected output:
# Reversing the string 'Hello': o l l e H
