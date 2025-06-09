from pathlib import Path
from modules.mostrar_categorias import mostrar_categorias
from modules.mostrar_recetas import mostrar_recetas
from modules.agregar_receta import agregar_receta
from modules.crear_categoria import crear_categoria
from modules.eliminar_receta import eliminar_receta
from modules.eliminar_categoria import eliminar_categoria
from modules.leer_receta import leer_receta

while True:
    print("\n" + "="*50)
    print("Bienvenido al recetario de 'Python'.")
    print("-"*50)
    mostrar_categorias()
    print("\nEste es nuestro menú de opciones:")
    print("1. Ver recetas de una categoría")
    print("2. Agregar nueva receta a una categoría")
    print("3. Crear una categoria nueva")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")  
    print("-"*50)
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        print("\n" + "-"*40)
        categoria = input("Ingrese el nombre de la categoría: ")
        mostrar_recetas(categoria)
        print("\n¿Cuál receta desea ver?")
        nombre_receta = input("Ingrese el nombre de la receta: ")
        print("\nContenido de la receta:")
        print("-"*40)
        leer_receta(categoria, nombre_receta)
        print("\n" + "-"*40)

    elif opcion == "2":
        print("\n" + "-"*40)
        categoria = input("Ingrese el nombre de la categoría: ")
        nombre_receta = input("Ingrese el nombre de la receta: ")
        print("Ingrese el contenido de la receta (escriba END en una línea nueva para finalizar):")
        lineas = []
        while True:
            linea = input()
            if linea.strip() == "END":
                break
            lineas.append(linea)
        contenido = "\n".join(lineas)
        agregar_receta(categoria, nombre_receta, contenido)
        print("\nReceta agregada exitosamente!\n" + "-"*40)

    elif opcion == "3":
        print("\n" + "-"*40)
        nombre_categoria = input("Ingrese el nombre de la nueva categoría: ")
        crear_categoria(nombre_categoria)
        print("\nCategoría creada exitosamente!\n" + "-"*40)

    elif opcion == "4":
        print("\n" + "-"*40)
        categoria = input("Ingrese el nombre de la categoría: ")
        nombre_receta = input("Ingrese el nombre de la receta a eliminar: ")
        eliminar_receta(categoria, nombre_receta)
        print("\nReceta eliminada exitosamente!\n" + "-"*40)
    
    elif opcion == "5":
        print("\n" + "-"*40)
        nombre_categoria = input("Ingrese el nombre de la categoría a eliminar: ")
        eliminar_categoria(nombre_categoria)
        print("\nCategoría eliminada exitosamente!\n" + "-"*40)
    
    elif opcion == "6":
        print("\nGracias por usar el recetario. ¡Hasta luego!\n" + "="*50)
        break
    else:
        print("\nOpción no válida. Intente de nuevo.\n" + "-"*40)





