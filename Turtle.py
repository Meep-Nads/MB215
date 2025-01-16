
# Simple Python code to demonstrate various Turtle functions

import turtle
import tkinter.simpledialog as simpledialog

# Set up the window
screen = turtle.Screen()
screen.bgcolor('White')

# Create a turtle
t = turtle.Turtle()
t.speed(1)
# Set pen size to 3
t.pensize(3)

# Set drawing color to blue
t.pencolor('blue')

# Move the turtle forward by 100 units
t.forward(100)

# Turn the turtle right by 90 degrees
t.right(90)

# Move the turtle forward by 50 units
t.forward(50)

# Turn the turtle left by 90 degrees
t.left(90)

# Lift the pen up – no drawing when moving
t.penup()

# Move the turtle to a specific location
t.setpos(-100,0)

# Put the pen down – drawing when moving
t.pendown()

# Draw a circle with radius of 25
t.circle(25)

# Draw a dot with diameter 10
t.dot(10)

# Set the turtle heading to 0 (East)
t.setheading(0)

# Change the turtle color
t.color('green')

# Draw a filled shape
t.hideturtle()
t.fillcolor('black')
t.begin_fill()
t.circle(15)
t.end_fill()

# Clear the drawing
t.clear()

# Reset the turtle's state
t.reset()

# Hide the turtle
t.hideturtle()

# Display the turtle
t.showturtle()

# Set the animation speed (0:fastest, 1:slowest, 10:normal)
t.speed(1)

# Display text
t.write('BOO')

# Get input with a dialog box
bananas = turtle.numinput('Input','Enter number of bananas')

# Respond to user input
t.write(f'You entered {bananas} bananas')

# Filling a shape with color
t.hideturtle()
t.fillcolor('red')
t.begin_fill()
t.circle(15)
t.end_fill()

# Close the window on a click
turtle.exitonclick()