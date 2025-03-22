#reate a Python program that manages a directory of countries and their respective capital cities.

    # Predefined dictionary with 10 countries and their capitals that I had to google the capitals for
country_capital = { 'Canada': 'Ottawa', 'Japan': 'Tokyo', 'France': 'Paris', 'Germany': 'Berlin', 'UK': 'London', 'Brazil': 'Brasília', 'Australia': 'Canberra', 'Italy': 'Rome', 'Mexico': 'Mexico City', 'Egypt': 'Cairo' }

print('Welcome to the Country-Capital Directory!')
    
    #Loop until exit is typed user inputs a country name, the program should look up and display the capital city
while True:
    country = input('Enter a country to find its capital city or type exit to quit: ')

    # make the input string not case sensitive
    if country.lower() == "exit":
        # User breaks the loop by typing exit
        print('Thank you for using the directory Goodbye!')
        break

    #Looks up capital city for the inputted country and prints both
    try:
        capital = country_capital[country]
        print(f'The capital city of {country} is {capital}')
    except KeyError:
        print('Sorry the country you are looking for is not in our directory')

