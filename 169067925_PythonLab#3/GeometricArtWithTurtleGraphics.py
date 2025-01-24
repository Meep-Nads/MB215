
# Import Turtle graphics library
import turtle

# Set up your drawing parameters
ITERATIONS = 5
NumCircles = 7
stem = 4
# The number of times to repeat the pattern
ANGLEs = 75
cAngle = 10
# The angle to turn after each shape is drawn
SIZE = 95
SIZES = 75
# The size parameter for the shapes

# Set up the Turtle screen and turtle customization
screen = turtle.Screen()
pattern_turtle = turtle.Turtle()
pattern_turtle.pencolor('Purple')
pattern_turtle.pensize(3)
pattern_turtle.fillcolor('Black')
pattern_turtle.speed(0)

# Loop to draw the big petal pattern
for i in range(ITERATIONS):
    # Set up fill
    pattern_turtle.hideturtle()
    pattern_turtle.fillcolor('Turquoise')
    pattern_turtle.begin_fill()

    # Draw a square:
    for _ in range(4):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(90)  # Right angle for a square
    pattern_turtle.end_fill()

    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(ANGLEs)
#Loop to draw the small petal pattern
for i in range(ITERATIONS):
    # Set up fill 
    pattern_turtle.hideturtle()
    pattern_turtle.fillcolor('Light Blue')
    pattern_turtle.begin_fill()
    
    # Draw a square:
    for _ in range(4):
        pattern_turtle.forward(SIZES)
        pattern_turtle.right(90)  # Right angle for a square
    pattern_turtle.end_fill()

    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(ANGLEs)

# Set up centre color
pattern_turtle.showturtle()
pattern_turtle.pencolor('Yellow')

    # Draw your circle centre pattern
for _ in range(NumCircles):
    pattern_turtle.circle(20)
    pattern_turtle.left(cAngle)
    pattern_turtle.circle(10)
    pattern_turtle.left(cAngle)

    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(ANGLEs)

# Creating the Stem
pattern_turtle.setheading(270)
pattern_turtle.penup()
pattern_turtle.forward(107)
pattern_turtle.pendown()
pattern_turtle.pencolor('Green')
pattern_turtle.pensize(20)
pattern_turtle.forward(115)

# Creating the leafs
pattern_turtle.setheading(135)
for _ in range(stem):
    pattern_turtle.forward(55)
    pattern_turtle.left(180)

pattern_turtle.setheading(45)
for _ in range(stem):
    pattern_turtle.forward(55)
    pattern_turtle.left(180)
    
# Complete the program with a command to keep the window open
turtle.done()
