from pathlib import Path

def mostrar_categorias():
    # Set the base path where categories are stored
    ruta_base = Path("D:/coding/recetario/Recetas")

    # List all directories (categories) in the base path
    categorias = [carpeta.name for carpeta in ruta_base.iterdir() if carpeta.is_dir()]

    print("Categorías disponibles:")
    # Print each category name
    for cat in categorias:
        print(f"- {cat}")