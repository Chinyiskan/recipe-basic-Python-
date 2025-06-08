from pathlib import Path

def mostrar_recetas(categoria):
    ruta_categoria = Path(f"D:/coding/recetario/Recetas/{categoria}")

    if not ruta_categoria.exists():
        print(f"La categoría '{categoria}' no existe.")
        return

    recetas = [archivo.name for archivo in ruta_categoria.iterdir() if archivo.is_file()]

    if not recetas:
        print(f"No hay recetas en la categoría '{categoria}'.")
        return

    print(f"Recetas en la categoría '{categoria}':")
    for receta in recetas:
        print(f"- {receta}")