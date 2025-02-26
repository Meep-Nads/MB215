#Activity 1: Define a Car Class
#Create a file named car.py and define a Car class with the following 
# Specifications:
# car.py

class Car:
    def __init__(self, make, model, year):
        # Your code here to initialize attributes
        # Store make attribute
        self._make = make
        #Call the private method to store the model
        self.__update_model(model) 
        # Store the year attribute
        self._year = year
        

    def display_info(self):
        # Your code here to print car details
        #Printing the make attribute
        print(f'Make = {self._make}')

        print(f'Model = {self._model}')
        print(f'Year = {self._year}')
        

    def __update_model(self, new_model):
        # Your code here to update the model
         self._model = new_model
        

    def __str__(self):
        # Your code here to return a string representation
        return f'{self._make} {self._model} {self._year}'

def compare_car_years(car1, car2):
    return car1._year < car2._year

# Your code here to define with values and print the comparison output
#Start excuting here
car1 = Car('Honda','Civic',2001)

car2 = Car('Toyota','Corolla',2010)

print(car1)
print(car2)
car1.display_info()
car2.display_info()

if compare_car_years(car1, car2):
    print(f'{car1} is older than {car2}')

else:
    print(f'{car1} is younger than {car2}')

