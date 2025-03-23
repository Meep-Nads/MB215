#As you train for an upcoming 10k run, track and calculate your average time over 5k practice runs

def main():
    #1.	Time Input: Prompt for the time taken (minutes and seconds) for each of five practice runs
    print('Input time for each 5k practice run')
    
    total_seconds = 0
    
    # Collect times for 5 runs
    for i in range(1, 6):
        while True:
            #Enter mins for each run
            minutes = int(input(f'Enter the minutes for run {i}: '))
            # mins are less than 0 print error message
            if minutes < 0:
                print('Minutes cannot be negative')
                continue
            break
        
        while True:
            # Enter seconds for each run
            seconds = int(input(f"Enter the seconds for run {i}: "))
            if seconds < 0 or seconds >= 60:
             # secs are less than 0 print error message
                print('Seconds should be between 0 and 59')
                continue
            break
        
    # Convert to total seconds
    total_seconds += ((minutes * 60) + seconds)

    # Calculate average seconds & minutes with no decimals
    average_seconds = total_seconds / 5
    avg_minutes = int(average_seconds / 60)
    #avg_remaining_seconds = round(average_seconds % 60)

    # Adjust if rounding seconds causes 60 seconds (rare case)
    if avg_remaining_seconds == 60:
        avg_minutes += 1
        avg_remaining_seconds = 0

#Print out the average minutes and seconds for 5 practive runs
    print('Calculating your average running time...')
    print(f'Your average running time is {avg_minutes} minutes and {avg_remaining_seconds} seconds')

# Call the main function to run program
if __name__ == "__main__":
    main()

