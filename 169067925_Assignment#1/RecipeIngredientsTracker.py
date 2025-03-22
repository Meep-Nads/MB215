#Develop a Python application that helps users keep track of ingredients for various recipes using Lists and Tuples

def display_menu():
    print("\nWelcome to the Recipe Ingredients Tracker!")
    print("\nPlease select an option:")
    print("1 - Add a New Recipe")
    print("2 - View a Recipe")
    print("3 - List All Recipes")
    print("4 - Remove a Recipe")
    print("0 - Exit")

def add_recipe(recipes):
    recipe_name = input("\nEnter the recipe name: ")
    ingredients_input = input("Enter the ingredients (separated by commas): ")
    ingredients_list = [ingredient.strip().capitalize() for ingredient in ingredients_input.split(",")]
    recipes.append((recipe_name, ingredients_list))
    print(f"\nRecipe '{recipe_name}' added successfully!")

def view_recipe(recipes):
    recipe_name = input("\nWhich recipe would you like to view? ")
    found = False
    for recipe in recipes:
        if recipe[0].lower() == recipe_name.lower():
            print(f"\nIngredients for '{recipe[0]}':")
            for ingredient in recipe[1]:
                print(f"- {ingredient}")
            found = True
            break
    if not found:
        print("Recipe not found.")

def list_all_recipes(recipes):
    if recipes:
        print("\nAll Recipes:")
        for idx, recipe in enumerate(recipes, start=1):
            print(f"{idx}. {recipe[0]}")
    else:
        print("\nNo recipes found.")

def remove_recipe(recipes):
    recipe_name = input("\nEnter the recipe name to remove: ")
    for recipe in recipes:
        if recipe[0].lower() == recipe_name.lower():
            recipes.remove(recipe)
            print(f"Recipe '{recipe[0]}' removed successfully!")
            return
    print("Recipe not found.")

def main():
    recipes = []

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            view_recipe(recipes)
        elif choice == "3":
            list_all_recipes(recipes)
        elif choice == "4":
            remove_recipe(recipes)
        elif choice == "0":
            print("\nThank you for using the Recipe Ingredients Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
