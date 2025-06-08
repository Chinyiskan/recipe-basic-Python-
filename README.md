# Python Recipe Book

This is a console-based Python program to manage a cooking recipe book. It allows you to organize recipes by category, add new recipes, create and delete categories, and read or delete existing recipes.

## Project Structure

- `main.py`: Main file that runs the interactive menu.
- `modules/`: Folder containing the main functions of the program.
- `Recetas/`: Folder where categories and recipes are stored as text files.

## Features

1. **View recipes in a category**: Shows available recipes in a category and lets you read their content.
2. **Add a new recipe to a category**: Allows you to create a new recipe within an existing category.
3. **Create a new category**: Creates a new folder for a recipe category.
4. **Delete a recipe**: Deletes a specific recipe from a category.
5. **Delete a category**: Deletes an entire category and all its recipes.
6. **Exit**: Ends the program.

## Requirements
- Python 3.7 or higher
- Compatible operating system (Windows recommended due to file paths)

## Usage
1. Clone or download this repository.
2. Run the main program:
   ```bash
   python main.py
   ```
3. Follow the menu instructions to manage your recipes.

## Notes
- Recipes are stored as `.txt` files inside category folders in the `Recetas/` directory.
- You can also manually add or edit categories and recipes by editing the files directly if you wish.

---
Enjoy organizing your recipes with Python!
