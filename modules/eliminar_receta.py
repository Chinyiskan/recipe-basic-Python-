from pathlib import Path

def eliminar_receta(categoria, nombre_receta):
    # Set the path for the recipe to delete
    ruta_receta = Path(f"D:/coding/recetario/Recetas/{categoria}/{nombre_receta}.txt")

    # Delete the recipe file if it exists
    if ruta_receta.exists():
        ruta_receta.unlink()
        print(f"Receta '{nombre_receta}' eliminada de la categoría '{categoria}'.")
    else:
        print(f"La receta '{nombre_receta}' no existe en la categoría '{categoria}'.")