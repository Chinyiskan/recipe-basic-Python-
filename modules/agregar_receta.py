from pathlib import Path 

def agregar_receta(categoria, nombre_receta, contenido):
    # Set the path for the new recipe file
    ruta_receta = Path(f"D:/coding/recetario/Recetas/{categoria}/{nombre_receta}.txt")

    # Write the content to the recipe file
    with open(ruta_receta, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    
    print(f"Receta '{nombre_receta}' agregada a la categoría '{categoria}'.")