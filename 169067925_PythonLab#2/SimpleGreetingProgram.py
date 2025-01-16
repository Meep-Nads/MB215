import datetime

# ask for user name
name = input('What is your name?')

# ask for user age
age = int(input('what is your age?'))

# print greeting
print(f'Nice to meet you {name}')

# calculate year user was born, then display it 
# note:must be 'year-age-1' because my birthday has not passed this year and therefore the calculation would be off by 1 year.
print(f'Your date of birth is: {datetime.datetime.now().year-age-1}')