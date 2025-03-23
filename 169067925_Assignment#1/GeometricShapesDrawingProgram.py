#Craft a Python program that uses the Turtle graphics library to draw various geometric shapes based on user input.
#Enhance your programming skills by creating interactive functions that will draw a square, triangle, circle, and rectangle using Turtle's drawing commands.

import turtle

# Function to draw a square
def draw_square(side_length, color):
    #Set up color for square
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

# Function to draw an equilateral triangle
def draw_triangle(side_length, color):
    # Set up color for triangle
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

# Function to draw a circle
def draw_circle(radius, color):
    # Set up color for circle
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    # Set up color for rectangle
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to get valid numeric input
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            #Error message for invalid inputs
            if value <= 0:
                print('Enter a positive number')
            else:
                return value
        except ValueError:
            print('Invalid input Enter a number')

# Main program menu options
def main():
    print('Welcome to the Turtle Shape Drawer!')
    print('Menu:')
    print('1 - Draw Square')
    print('2 - Draw Triangle')
    print('3 - Draw Circle')
    print('4 - Draw Rectangle')
    print('0 - Exit')

    # User input for menu options
    choice = input('Enter your choice: ')

    # Draw square with user inputted parameters
    if choice == "1":
        side = get_positive_number("Enter the side length of the square: ")
        color = input("Enter the color of the square: ")
        draw_square(side, color)

    # Draw triangle with user inputted parameters
    elif choice == "2":
        side = get_positive_number("Enter the side length of the triangle: ")
        color = input("Enter the color of the triangle: ")
        draw_triangle(side, color)

    # Draw circle with user inputted parameters
    elif choice == "3":
        radius = get_positive_number("Enter the radius of the circle: ")
        color = input("Enter the color of the circle: ")
        draw_circle(radius, color)

    # Draw rectangle with user inputted parameters
    elif choice == "4":
        width = get_positive_number("Enter the width of the rectangle: ")
        height = get_positive_number("Enter the height of the rectangle: ")
        color = input("Enter the color of the rectangle: ")
        draw_rectangle(width, height, color)

    # Exit the program
    elif choice == "0":
        print("Goodbye!")
        return

    # Invalid choice message
    else:
        print("Invalid choice. Please select a valid option.")
        return

    # Keep the window open until clicked
    turtle.done()

# Call the main function to run the program
if __name__ == "__main__":
    main()
