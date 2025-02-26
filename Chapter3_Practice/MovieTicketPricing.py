#Ask the user for their age and whether they are a student (yes/no).
#Ticket price: Children (under 12): Free Students (any age): $8 Adults (12–59): $12 Seniors (60+): $6
#Print the final ticket price.
#Bonus: Use a ternary operator for the student discount.

age = int(input('Enter Age: '))
student = input('Are you a Student? ')

if student == 'yes':
    print('Student Price = $8')
else:
    if age <= 0:
        print('Children price = $0')
    elif age in range(12,60):
        print('Adult Price = $12')
    else:
        print('Seniors Pricing = $6')


#Write a program that simulates a movie ticket purchase system.
#The system should keep track of the number of tickets purchased, calculate the total price, 
#and handle various conditions such as valid input, applying discounts, and offering the user the chance to change their mind. 
#The program should use loops, functions, conditional expressions, and variable manipulation.

#Price Calculation: A standard movie ticket costs $12. If the user buys more than 5 tickets, they get a 10% discount on the total price.
ticket = 12

def calculate_total(tickets):
    num = int(input('Enter Amount of Tickets:'))
#Input Validation: The program should ask the user how many tickets they want to buy. 
#If the input is invalid (e.g., a negative number or non-integer), the program should prompt them again. The program should continue asking until the user provides a valid number of tickets.

#Sentinels:The program should allow the user to stop purchasing more tickets by entering a sentinel value of -1.

#Nested Loops:After the user enters a valid number of tickets, the system should ask if they want to add more tickets. This loop should continue until the user enters -1 to stop.

#Functions: Define functions for calculating the total price and applying the discount.Use local variables inside the functions.Use a global constant for the price of one ticket.

#Break, Continue, and Else:Use break when the user enters -1 to stop the program. Use continue to skip invalid inputs and prompt again. Use an else statement in the loop to show the total after valid input.

#Boolean Variables & Logical Operators: Implement a Boolean variable to check if the user qualifies for the discount.