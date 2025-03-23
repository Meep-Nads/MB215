#Question 3. Letters before “m” in the alphabet and “m” or after

#Create a Python program with two distinct functions to count occurrences of letters in a string based on their position in the alphabet relative to the letter 'm'.


#1.	Function count_before_m:
def count_before_m(s):
    count = 0
    # make case insensitive
    for char in s.lower():
        #It will return the count of all letters within the string that come before 'm' in the alphabet.
        if char.isalpha() and char < 'm':
            count += 1
    return count

#2.	Function count_m_and_after:
def count_m_and_after(s):
    count = 0
    # make case insensitive
    for char in s.lower():
        #It will return the count of all letters within the string that are 'm' or come after 'm' in the alphabet
        if char.isalpha() and char >= 'm':
            count += 1
    return count

# Main function to enter the string to be counted
def main():
    user_input = input("Please enter a string: ")

    #Runs the before m count function using the user input
    before_m_count = count_before_m(user_input)
    #Runs the at and after m count function using the user input
    m_and_after_count = count_m_and_after(user_input)

    #Prints resluts of the two counts functions
    print(f"\nNumber of letters before 'm' in the alphabet: {before_m_count}")
    print(f"Number of letters 'm' or after in the alphabet: {m_and_after_count}")

# Calls the above functions
if __name__ == "__main__":
    main()