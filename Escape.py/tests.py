print('Access Granted')
print('.... Loading .....')
print('Facility Door Override Access Codes:')
print('0 - Emergency protocals')
print('1 - One Market')
print('2 - Grand River Hall')
print('3 - Market Darling')
print('4 - Odeon')
print('5 - Research Academic Centre West')
print('6 - Research Academic Centre East')
file = input(f'Select Building: ')
if file == '1':
    print('4444')
elif file == '2':
    print('2')
elif file == '3':
    print('3')
elif file == '4':
    print('4')
elif file == '5':
    print('5')
elif file == '6':
    print('6')
else:
    print('Unable to find file')