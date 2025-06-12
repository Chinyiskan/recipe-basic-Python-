from pathlib import Path


def leer_receta(categoria, nombre_receta):
    # Set the path for the recipe to read
    ruta_receta = Path(f"D:/coding/recetario/Recetas/{categoria}/{nombre_receta}.txt")

    # Read and print the content of the recipe file
    if ruta_receta.exists():
        with open(ruta_receta, "r", encoding="utf-8") as archivo:
            print(archivo.read())
    else:
        print("Recipe not found.")