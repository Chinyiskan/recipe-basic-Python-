from pathlib import Path


def leer_receta(categoria, nombre_receta):
    ruta_categoria = Path(f"D:/coding/recetario/Recetas/{categoria}")

    if not ruta_categoria.exists():
        print(f"La categoría '{categoria}' no existe.")
        return

    ruta_receta = ruta_categoria / f"{nombre_receta}.txt"

    if not ruta_receta.exists():
        print(f"La receta '{nombre_receta}' no existe en la categoría '{categoria}'.")
        return

    with open(ruta_receta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    
    print(f"Contenido de la receta '{nombre_receta}':\n{contenido}")