from pathlib import Path

def eliminar_categoria(nombre_categoria):
    # Set the path for the category to delete
    ruta_categoria = Path(f"D:/coding/recetario/Recetas/{nombre_categoria}")

    # Delete the category directory and all its contents if it exists
    if ruta_categoria.exists() and ruta_categoria.is_dir():
        for archivo in ruta_categoria.iterdir():
            archivo.unlink()  # Delete each file in the category
        ruta_categoria.rmdir()  # Remove the category directory

        print(f"Categoría '{nombre_categoria}' eliminada exitosamente.")
    else:
        print(f"La categoría '{nombre_categoria}' no existe.")
