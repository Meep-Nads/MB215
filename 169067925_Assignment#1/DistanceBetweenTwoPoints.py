#Develop a function in Python to determine if two spherical balls on a flat surface are in contact with each other.

#The contact between two balls is established by calculating the distance between their centers.
#The coordinates (x1, y1) and (x2, y2) represent the centers of the first and second balls, respectively.
#To determine the distance, we apply the Pythagorean theorem as follows:
#distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#When the sum of the radii of both balls is greater than or equal to this distance, it implies that the balls are touching.

#Task Description:
import math
#Input for corrdinates and radius calculation for Ball1 and Ball2
#Input the y-corrdinate for ball 1
ball1_xcor = int(input('Enter x-coordinate for ball 1:'))

#Input the y-corrdinate for ball 1
ball1_ycor = int(input('Enter y-coordinate for ball 1:'))

#Input radius for ball 1
ball1_radius = int(input('Enter radius for ball 1:'))

#Input the x-corrdinate for ball 2
ball2_xcor = int(input('Enter x-coordinate for ball 2:'))

#Input the y-corrdinate for ball 2
ball2_ycor = int(input('Enter y-coordinate for ball 2:'))

#Input radius for ball 2
ball2_radius = int(input('Enter radius for ball 2:'))

#Output x, y and radius inputs for ball 1
print(f'Ball 1 = Center: {(ball1_xcor,ball1_ycor)}, Radius: {ball1_radius}')

#Output x, y and radius inputs for ball 2
print(f'Ball 2 = Center: {(ball2_xcor,ball2_ycor)}, Radius: {ball2_radius}')

#Calculate the distance between the center of the balls
distance = math.sqrt((ball2_xcor - ball1_xcor)**2 + (ball2_ycor - ball1_ycor)**2)

#Print the distance between the center of the balls
print(f'Distance between centers: {distance}')

#Output whether the balls are touching or not.
if distance <= ball1_radius + ball2_radius:
    print('Result: The balls are touching.')
else:
    print('Result: The balls are not touching.')





#Expected Output:
#Your program should display the following:
#•	The x, y coordinates and radius for each ball as entered by the user.
#•	The calculated distance between the centers of the two balls.
#•	A statement indicating whether the balls are touching or not.
#Sample Output:
#Enter x-coordinate for ball 1: 4
#Enter y-coordinate for ball 1: 4
#Enter radius for ball 1: 3
#Enter x-coordinate for ball 2: 10
#Enter y-coordinate for ball 2: 5
#Enter radius for ball 2: 4

#Ball 1: Center = (4, 4), Radius = 3
#Ball 2: Center = (10, 5), Radius = 4
#Distance between centers: 6.082762530298219
#Result: The balls are touching.
