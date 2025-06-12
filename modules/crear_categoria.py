from pathlib import Path

def crear_categoria(nombre_categoria):
    # Set the path for the new category
    ruta_categoria = Path(f"D:/coding/recetario/Recetas/{nombre_categoria}")

    # Create the directory for the new category if it doesn't exist
    ruta_categoria.mkdir(exist_ok=True)

    if ruta_categoria.exists():
        print(f"La categoría '{nombre_categoria}' ya existe.")
        return

    ruta_categoria.mkdir(parents=True, exist_ok=True)
    print(f"Categoría '{nombre_categoria}' creada exitosamente.")