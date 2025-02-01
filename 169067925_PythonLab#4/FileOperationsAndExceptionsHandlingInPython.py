import traceback
# Activity 1: Writing to a File. This code is provided to you to show how #to write to a file, the use if try except for exception handling and the #use of traceback
def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
            file.close()

    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

# Activity 2: Reading from a File
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            file.read(filename)
            file.close()
    except Exception as e:
        print(f"An error occurred while reading to the file: {filename}")
        traceback.print_exc()
    


# Activity 3: Appending to a File
def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data)
            file.close()

    except Exception as e:
        print(f"An error occurred while appending to the file: {filename}")
        traceback.print_exc()
   
__name__ = input('Enter Action you would like to do: ')
# Demonstrating the functions
if __name__ == "write":
    # Writing to a file
    write_to_file('sample.txt', 'Hello, World!\n')
    
    # Reading from a file
     #write missing code here.
    
    # Appending to a file
      #write missing code here.

# Trying to read from a non-existent file to demonstrate exception handling
    non_existent_content = read_from_file('non_existent_file.txt')
    if non_existent_content is None:
        print("Could not read the non-existent file.")
