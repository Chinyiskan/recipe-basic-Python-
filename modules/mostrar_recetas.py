from pathlib import Path

def mostrar_recetas(categoria):
    # Set the path for the selected category
    ruta_categoria = Path(f"D:/coding/recetario/Recetas/{categoria}")

    # Check if the category exists
    if not ruta_categoria.exists():
        print(f"La categoría '{categoria}' no existe.")
        return

    # List all recipe files in the category
    recetas = [archivo.name for archivo in ruta_categoria.iterdir() if archivo.is_file()]

    # Check if there are no recipes in the category
    if not recetas:
        print(f"No hay recetas en la categoría '{categoria}'.")
        return

    print(f"Recetas en la categoría '{categoria}':")
    # Print each recipe name
    for receta in recetas:
        print(f"- {receta.replace('.txt', '')}")