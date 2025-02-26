#Ask the user to enter a username and password.
#If the username is "admin" (case insensitive) and the password is "admin123", print "Login Successful".
#Otherwise, print "Invalid credentials".
#💡 Bonus: Allow the user three attempts before locking them out.
for attempt in range(3):
    username = input('Enter Username: ')
    password = input('Enter Password: ')

    if username == 'admin' and password == 'admin123':
        print('Login Successful')
        break
    else:
        print('Invaild Credentials')

else:
    print('Account Locked')
