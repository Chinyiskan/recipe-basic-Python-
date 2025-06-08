from pathlib import Path

def eliminar_categoria(nombre_categoria):
    ruta_base = Path("D:/coding/recetario/Recetas")
    ruta_categoria = ruta_base / nombre_categoria

    if not ruta_categoria.exists():
        print(f"La categoría '{nombre_categoria}' no existe.")
        return

    for archivo in ruta_categoria.iterdir():
        archivo.unlink()  # Elimina los archivos dentro de la categoría
    ruta_categoria.rmdir()  # Elimina la carpeta de la categoría

    print(f"Categoría '{nombre_categoria}' eliminada exitosamente.")
