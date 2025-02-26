#Basic: Write an if statement that prints "Hello, World!" if a variable x is equal to 10.
x= int(input('Enter number: '))

if x == 10:
   print('Hello, World')
else:
   print('Error.1')

#Intermediate: Write a program that checks if a number is positive, negative, or zero and prints an appropriate message.
num = int(input('Enter a number: '))

if num >= 0:
   print(f'{num} is a Positive Number')
elif num <= 0:
   print(f'{num} is a Negative Number')
elif num == 0:
   print(f'{num} is 0')
else:
   print('Error.2')

#Advanced: Create a program that asks the user for their age and then prints out if they are a child, teenager, adult, 
#or senior based on their input.

age = int(input('Enter your age: '))

if age in range(0,13):
   print('You are a Child')
elif age in range(13,18):
   print('You are a Teenager')
elif age in range(18,65):
   print('You are an Adult')
elif age >= 65:
   print('You are a Senior')
else:
   print('Error.3')