#Develop a function in Python to determine if two spherical balls on a flat surface are in contact with each other.
#The contact between two balls is established by calculating the distance between their centers. The coordinates (x1, y1) and (x2, y2) represent the centers of the first and second balls, respectively. To determine the distance, we apply the Pythagorean theorem as follows:
#distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#When the sum of the radii of both balls is greater than or equal to this distance, it implies that the balls are touching.
#Task Description:
#1.	Input the x, y and radius of 2 balls
#2.	Output the x, y and radius as they were input
#3.	Output the distance between the center of the balls
#4.	Output whether the balls are touching or not.
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
