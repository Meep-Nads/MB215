#Intermediate: Nested Decisions, Modify the test score program so that:
#If the score is below 60, check if the student has submitted extra credit work (yes or no input).
#If yes, print "You passed with extra credit!", otherwise "You failed.".

score = int(input("Enter your test score: "))
extra = (input('Did you Submit Extra Credit Work? '))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    if extra == 'Yes':
        print('You Passed with extra credit!')
    else:
        print('You Failed')


#Advanced: Multiple Conditions
#Write a program that:
#Asks the user for their income and credit score.
#If income is above 50,000 and credit score is above 700, print "Loan Approved!".
#Otherwise, print  "Denied."

income = int(input('Enter your Income: $'))
credit = int(input('Enter your Credit Score: '))

if income >= 50000 and credit >= 700:
    print('Loan Approved!')
else:
    print('Denied')