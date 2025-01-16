import datetime

# ask for user name
name = input('What is your name?')

# ask for user age
age = int(input('what is your age?'))

# print greeting
print('Nice to meet you',name)

# calculate year user was born, then display it
print(f'You were born in {datetime.datetime.now().year-age-1}')