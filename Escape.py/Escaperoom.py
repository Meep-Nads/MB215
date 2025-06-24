data = [
    ["Name", "Department", "Role", "E-Mail", "ID"],
    ["Lottie Curry", "Environmental Health & Safety", "Environmental Officer", "enviro@wlu.ca", "468372922"],
    ["Byro Castro", "Campus Facilities Operations", "Operations Manager", "campusaccesscontrol@wlu.ca", "589683129"],
    ["Kent Mcgee", "Campus Security Services", "Special Constable", "campussecurity@wlu.ca", "192438056"],
    ["Clarie Whitaker", "Environmental Health & Safety", "HR", "hr@wlu.ca", "852870501"],
    ["Deborah MacLatchy", "Campus Facilities Operations", "Special Constable", "campusaccesscontrol@wlu.ca", "674263928"],
    ["Issac Collier", "Campus Transit Office", "Communications Officer", "commstrans@wlu.ca", "909562679"],
    ["Jeffery Norris", "Emergency Management Services", "IT Support", "emergserv@wlu.ca", "616783760"],
    ["Carlos Jamison", "Custodial Services", "Custodian", "custserv@wlu.ca", "567421917"]
]

# Determine column widths
col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]




uniname = input('Enter Unversity Name: ')

adminsyst = input('Enter Administration System to Access: ')
department = input('Enter Department: ')
if adminsyst == 'Faculty & Staff Portal' and department == 'Custodial Services':
    name = input('Enter Name: ')
        #role = input('Enter Role: ')
    idnum = input('Enter ID: ')
    if name == 'Carlos Jamison' and idnum == '567421917':
        # Print the table
        for i, row in enumerate(data):
            row_str = " | ".join(f"{str(val).ljust(col_widths[j])}" for j, val in enumerate(row))
            print(row_str)
            if i == 0:
                print("-+-".join("-" * w for w in col_widths))
    else:
        print('Invaild Credentials')
elif adminsyst == 'Building Access Control System' and department == 'Campus Facilities Operations':
    intsyst = input('Enter Internal System Name: ')
    if intsyst == 'eCampo/Fsyst':
        role = input('Enter Role: ')
        if role == 'Special Constable':
            email = input('Enter E-mail: ')
            if email == 'campusaccesscontrol@wlu.ca':
                user = input('Enter User Name: ')
                if user == 'Deborah MacLatchy':
                    idnum = input('Enter ID: ')
                    if idnum == '674263928':
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
                        file = input('Select Building: ')
                        if file == 1:
                            print('1')
                        elif file == 2:
                            print('2')
                        elif file == 3:
                            print('3')
                        elif file == 4:
                            print('4')
                        elif file == 5:
                            print('5')
                        elif file == 6:
                            print('6')
                        else:
                            print('Unable to find file')
                    else: 
                        print('Invaild ID')
                else:
                    print('Invaild name')
            else:
                print('Invaild email')
        else:
            print('Invaild role')
    else:
        print('Invaild internal system name')
else:
    print('Invaild input')



