#Construct a Python program that randomly selects an exercise by simulating a toss of a triangular pyramid, each face representing a different exercise.
#Your program should virtually "toss" a triangular pyramid, where each side corresponds to an exercise written on it, and output the selected exercise.

import random

def toss_pyramid():
    # Define the edges of the pyramid
    exercises = ['Plank', 'Squat', 'Sit-up', 'Push-up']
    # Randomly toss the pyramid to select the exercise
    selected_exercise = random.choice(exercises)
    #Print the exercise
    print(f'Tossing the pyramid...')
    print(f'You should do: {selected_exercise}')

# Function to prompt the user to roll the pyramid
def main():
    print("Welcome to the Exercise Pyramid Toss!")
    
    while True:
        # Prompt user to toss or exit, remove any whitespaces and make not case sensitive
        user_input = input('Press Enter to toss the pyramid or Type exit to quit: ').strip().lower()
        # Check if user wants to exit
        if user_input == 'exit':
            print('Goodbye! Stay active!')
            break
        # If user wants to toss the pyramid
        else:
            toss_pyramid()

#call the main function
if __name__ == "__main__":
    main()
