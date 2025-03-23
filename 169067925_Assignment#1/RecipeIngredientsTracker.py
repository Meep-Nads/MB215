#Develop a Python application that helps users keep track of ingredients for various recipes using Lists and Tuples

# Function to display the menu and different options
def display_menu():
    print('Welcome to the Recipe Ingredients Tracker!')
    print('Select an option: ')
    print('1 - Add a New Recipe')
    print('2 - View a Recipe')
    print('3 - List All Recipes')
    print('4 - Remove a Recipe')
    print('0 - Exit')

# Function to Add a New Recipe: Input a recipe name and its associated ingredients
def add_recipe(recipes):
    recipe_name = input('Enter the recipe name: ')
    ingredients_input = input('Enter the ingredients (separated by commas): ')
    # Format the strings, remove all the whitespace, capitalize and split the ingredients with a comma
    ingredients_list = [ingredient.strip().upper() for ingredient in ingredients_input.split(",")]
    # Add the list of ingredients to the recipe list
    recipes.append((recipe_name, ingredients_list))
    print(f'Recipe {recipe_name} added successfully!')

# Function to view the recipe list
def view_recipe(recipes):
    recipe_name = input('Enter recipe name to view:')
    found = False
    for recipe in recipes:
        # If recipe name in recipe is the same as recipe name entered regardless of case sensitivity, print the recipe ingredients list
        if recipe[0].lower() == recipe_name.lower():
            print(f'Ingredients for {recipe[0]}:')
            for ingredient in recipe[1]:
                print(f' - {ingredient}')
            found = True
            break
    if not found:
        print('Recipe not found')

# Function to list all recipes in the recipe list, if any exist
def list_all_recipes(recipes):
    #List all the recipes currently stored
    if recipes:
        print('All Recipes:')
        # Format list of all recipes
        for idx, recipe in enumerate(recipes, start=1):
            print(f"{idx}. {recipe[0]}")
    else:
        print('No recipes found')

# Function to remove a recipe from the recipe list, if it exists in the list
def remove_recipe(recipes):
    recipe_name = input('Enter the recipe name to remove: ')
    for recipe in recipes:
        # If recipe name in recipe is the same as recipe name entered regardless of case sensitivity, remove the recipe from the list
        if recipe[0].lower() == recipe_name.lower():
            recipes.remove(recipe)
            print(f"Recipe '{recipe[0]}' removed successfully!")
            return
    print("Recipe not found.")

# Main function to run the application and display the menu options
def main():
    recipes = []

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        # If 1 then run add recipe function
        if choice == "1":
            add_recipe(recipes)
        # If 2 then run view recipe function
        elif choice == "2":
            view_recipe(recipes)
        # If 3 then run list all recipes function
        elif choice == "3":
            list_all_recipes(recipes)
        # If 4 then run remove recipe function
        elif choice == "4":
            remove_recipe(recipes)
        # If 0 then exit the program
        elif choice == "0":
            print("\nThank you for using the Recipe Ingredients Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Call on the above programs to start
if __name__ == "__main__":
    main()
