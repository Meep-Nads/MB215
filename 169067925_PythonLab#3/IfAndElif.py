# Write a Python program that converts a numeric grade into its corresponding letter grade
# Use the following instructions:
# Convert the numeric grade into a letter grade based on the following scale:
# A+: 90 and above, A: 80 to 89, B: 70 to 79, C: 60 to 69, D: 50 to 59, F : Below 50
# Output the letter grade to the user.

# Ask the user to input a numeric grade.
nGrade = float(input("Enter your numeric grade:"))

# Convert the numeric grade into a letter g
# Ask Clara what she did
if nGrade >= 90:
    lGrade = "A+"
    print(f'Your letter grade is: {lGrade}')
elif nGrade >= 80 and nGrade <= 89:
    lGrade = "A"
    print(f'Your letter grade is: {lGrade}')
elif nGrade >= 70 and nGrade <= 79:
    lGrade = "B"
    print(f'Your letter grade is: {lGrade}')
elif nGrade >= 60 and nGrade <= 69:
    lGrade = "C"
    print(f'Your letter grade is: {lGrade}')
elif nGrade >= 50 and nGrade <= 59:
    lGrade = "D"
    print(f'Your letter grade is: {lGrade}')
elif nGrade <= 50:
    lGrade = "F"
    print(f'Your letter grade is: {lGrade}')