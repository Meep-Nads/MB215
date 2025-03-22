#Question 3. Letters before “m” in the alphabet and “m” or after

#Create a Python program with two distinct functions to count occurrences of letters in a string based on their position in the alphabet relative to the letter 'm'.
#Task Description:
#1.	Function count_before_m:
#o	This function will take a single string argument.
def count_before_m(string):
    count = 0
    #o	It will return the count of all letters within the string that come before 'm' in the alphabet.
    for char in string:
        if char.lower() < 'm':
            count += 1

#2.	Function count_m_and_after:
    #o    This function will also take a single string argument.
def count_m_and_after(string):
    count = 0
    #o	It will return the count of all letters within the string that are 'm' or come after 'm' in the alphabet.
    for char in string:
        if char.lower() >= 'm':
            count += 1

#3.	User Input:
#o	Prompt the user to enter a string.
string = input('Enter a string: ')

#o	Ensure that the string is evaluated case-insensitively, meaning 'M' and 'm' are treated equally.
string = string.lower()

#4.	Output Display:
#o	Using the input string, call both functions and display the results.
def main():
#o	Show the user the count of letters before 'm' and the count of letters 'm' and after.
   print (f"Number of letters before 'm' in the alphabet: {count_before_m} characters")
# the count of letters 'm' and after.
   print (f"Number of letters 'm' or after in the alphabet: {count_m_and_after} characters")
#Sample output:
#Please enter a string: Amazingly few discotheques provide jukeboxes.

#Number of letters before 'm' in the alphabet: 24
#Number of letters 'm' or after in the alphabet: 2


def count_before_m(s):
    count = 0
    for char in s.lower():
        if char.isalpha() and char < 'm':
            count += 1
    return count

def count_m_and_after(s):
    count = 0
    for char in s.lower():
        if char.isalpha() and char >= 'm':
            count += 1
    return count

def main():
    user_input = input("Please enter a string: ")

    before_m_count = count_before_m(user_input)
    m_and_after_count = count_m_and_after(user_input)

    print(f"\nNumber of letters before 'm' in the alphabet: {before_m_count}")
    print(f"Number of letters 'm' or after in the alphabet: {m_and_after_count}")

if __name__ == "__main__":
    main()
