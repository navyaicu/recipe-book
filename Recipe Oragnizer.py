class Recipe:
    def __init__(self, name, ingredients, instructions, category):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category

class RecipeOrganizer:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def view_all_recipes(self):
        for recipe in self.recipes:
            print(f"\n{recipe.name} ({recipe.category})")

    def view_recipe_details(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                print(f"\n{recipe.name} ({recipe.category})")
                print("Ingredients: ", ', '.join(recipe.ingredients))
                print("Instructions: ", recipe.instructions)
                return
        print(f"No recipe found with the name '{recipe_name}'.")

    def search_by_category(self, category):
        matching_recipes = [recipe for recipe in self.recipes if recipe.category.lower() == category.lower()]
        if matching_recipes:
            for recipe in matching_recipes:
                print(f"\n{recipe.name} ({recipe.category})")
                print("Ingredients: ", ', '.join(recipe.ingredients))
                print("Instructions: ", recipe.instructions)
        else:
            print("No recipes found in this category.")

    def delete_recipe(self, recipe_name):
        self.recipes = [recipe for recipe in self.recipes if recipe.name.lower() != recipe_name.lower()]
        print(f"Recipe '{recipe_name}' deleted successfully!")

def main():
    organizer = RecipeOrganizer()

    while True:
        print("\nRecipe Organizer Menu:")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. View Recipe Details")
        print("4. Search by Category")
        print("5. Delete Recipe")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions: ")
            category = input("Enter category: ")

            new_recipe = Recipe(name, ingredients, instructions, category)
            organizer.add_recipe(new_recipe)
            print("Recipe added successfully!")

        elif choice == '2':
            organizer.view_all_recipes()

        elif choice == '3':
            recipe_name = input("Enter recipe name to view details: ")
            organizer.view_recipe_details(recipe_name)

        elif choice == '4':
            category = input("Enter category to search: ")
            organizer.search_by_category(category)

        elif choice == '5':
            recipe_name = input("Enter recipe name to delete: ")
            organizer.delete_recipe(recipe_name)

        elif choice == '6':
            print("Exiting Recipe Organizer. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
