import datetime
name = input('What is your name?')
age = int(input('what is your age?'))
print('Nice to meet you',name)
print(f'You were born in {datetime.datetime.now().year-age-1}')