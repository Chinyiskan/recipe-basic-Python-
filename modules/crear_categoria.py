from pathlib import Path

def crear_categoria(nombre_categoria):
    ruta_base = Path("D:/coding/recetario/Recetas")
    ruta_categoria = ruta_base / nombre_categoria

    if ruta_categoria.exists():
        print(f"La categoría '{nombre_categoria}' ya existe.")
        return

    ruta_categoria.mkdir(parents=True, exist_ok=True)
    print(f"Categoría '{nombre_categoria}' creada exitosamente.")