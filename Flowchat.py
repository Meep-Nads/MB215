# Activity 8: Flowchart to Python Code
# The bellow flowchart outlines a simple program for calculating gross pay based on hours worked and hourly pay rate. 
# Write and run the python code that correspond to this flowchart below:
# Start -> Input hours worked -> Input hourly pay rate -> Calculate gross pay (hours worked * Pay rate) -> Display Gross pay -> End

# Input hours worked
Hours = int(input('Enter number of hours worked'))

# Input hourly pay rate
Prate = float(input('Enter hourly pay rate'))

# Calculate gross pay (hours worked * Pay rate)
GrossPay = Hours * Prate

# Display Gross pay
print(f'Your Gross Pay is: ${GrossPay:.2f}')