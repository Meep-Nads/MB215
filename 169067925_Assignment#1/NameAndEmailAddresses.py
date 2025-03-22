#Create a Python program that serves as an email directory, allowing users to manage email addresses associated with names.

#Your program should utilize a dictionary to store names and email addresses as key-value pairs. It must provide a 

# Function to provide menu with options to perform the following actions:
def display_menu():
    print('Menu Options:')
    # Exit Program: Terminate the program.
    print('0 - Exit Program')
    # Look Up an Email Address: Search for a person's email by their name.
    print('1 - Look Up an Email Address')
    # Add a New Contact: Input a new name and their email address to the directory.
    print('2 - Add a New Contact')
    # Update an Existing Contact: Modify an existing person's email address.
    print('3 - Update an Existing Contact')
    # Remove a Contact: Delete a person's name and email address from the directory.
    print('4 - Remove a Contact')
    # Display All Contacts: Show a list of all names and email addresses in the directory.
    print('5 - Display All Contacts')
    # List Email Addresses: Integrate a method to display all email addresses stored in the dictionary.
    print('6 - List All Email Addresses')

#Function to look up contact information
def look_up_contact(directory):
    #Ask for name to look up
    name = input('Enter name: ')
    # print name found in directory
    if name in directory:
        print(f'The email address is {directory[name]}')
    else:
        print('Contact not found')

#Function to add contacts into the directory
def add_contact(directory):
    name = input('Enter the name: ')
    #Display contact already in the directory if name is found in the directory
    if name in directory:
        print('This contact already exists')
    # Add the contact to the directory
    else:
        email = input('Enter the email: ')
        directory[name] = email
        print(f'Contact added: {directory}')

# Function to update contact in the directory
def update_contact(directory):
    name = input('Enter name to update: ')
    #If name is already in the directory, replace it with new name
    if name in directory:
        email = input('Enter new email address: ')
        directory[name] = email
        print('Contact updated')
    # If name is not in the directory, print contact not found
    else:
        print('Contact not found')

#Function to remove contact from the directory
def remove_contact(directory):
    name = input('Enter name to remove: ')
    # If name is in the directory, remove it from the directory, else print contact not found
    if name in directory:
        del directory[name]
        print('Contact removed')
    # If name is not in the directory, print contact not found
    else:
        print('Contact not found')

#function to display all contact information
def display_all_contacts(directory):
    # Print all contracts name and email in directory
    if directory:
        print('All Contacts:')
        for name, email in directory.items():
            print(f'{name}: {email}')
    else:
        print('No contacts found')

#function to list all email addresses in directory
def list_email_addresses(directory):
    # Print all email addresses in directory, if directory is not empty, else print no email addresses found.
    if directory:
        print('All Email Addresses: ')
        for email in directory.values():
            print(email)
    else:
        print('No email addresses found')

# Function for email directory
def main():
    email_directory = {}

    while True:
        # Display menu and get user choice
        display_menu()
        choice = input('Enter your choice > ')
        #If enters 0 exit program
        if choice == "0":
            print('Exiting program Goodbye!')
            break
        #If enters 1 run look up contact function
        elif choice == "1":
            look_up_contact(email_directory)
        #If enters 2 run add contact function
        elif choice == "2":
            add_contact(email_directory)
        #If enters 3 run update contact function
        elif choice == "3":
            update_contact(email_directory)
        #If enters 4 run remove contact function
        elif choice == "4":
            remove_contact(email_directory)
        #If enter 5 run display all contact function
        elif choice == "5":
            display_all_contacts(email_directory)
         #If enters 6 run list all email addresses function
        elif choice == "6":
            list_email_addresses(email_directory)
        else:
            print('Select a valid option')

# Define the function to run
if __name__ == "__main__":
    main()
