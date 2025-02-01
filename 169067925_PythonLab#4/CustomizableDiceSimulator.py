import random

# Activity 1: Customizable Dice Simulator
def roll_dice(num_dice, num_sides):
    total = 0

    #Loop for dice roll based on num of dice inputed
    for num in range(num_dice):
        a = 0

        #determining dice roll based on num of sides inputed
        a = random.randint(1, num_sides)
        
        #add dice roll to total 
        total += a
    return total

#Input for how many dice to roll
num_dice = int(input('How many dice would you like to roll: '))

#Input for many sides each dice should have
num_sides = int(input('Enter amount of dice sides: '))

#print sum of all dice rolled 
print(f'Rolling {num_dice} D{num_sides} ... Result is {roll_dice(num_dice, num_sides)}')

 