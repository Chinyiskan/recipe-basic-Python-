from pathlib import Path

def mostrar_categorias():
    ruta_base = Path("D:/coding/recetario/Recetas")

    categorias = [carpeta.name for carpeta in ruta_base.iterdir() if carpeta.is_dir()]

    print("Categorías disponibles:")
    for cat in categorias:
        print(f"- {cat}")