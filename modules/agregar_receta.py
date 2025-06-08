from pathlib import Path 

def agregar_receta(categoria, nombre_receta, contenido):
    ruta_categoria = Path(f"D:/coding/recetario/Recetas/{categoria}")

    if not ruta_categoria.exists():
        print(f"La categoría '{categoria}' no existe.")
        return

    ruta_receta = ruta_categoria / f"{nombre_receta}.txt"

    if ruta_receta.exists():
        print(f"La receta '{nombre_receta}' ya existe en la categoría '{categoria}'.")
        return

    with open(ruta_receta, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    
    print(f"Receta '{nombre_receta}' agregada a la categoría '{categoria}'.")