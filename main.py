from pathlib import Path
# Import main functions from each module
from modules.mostrar_categorias import mostrar_categorias
from modules.mostrar_recetas import mostrar_recetas
from modules.agregar_receta import agregar_receta
from modules.crear_categoria import crear_categoria
from modules.eliminar_receta import eliminar_receta
from modules.eliminar_categoria import eliminar_categoria
from modules.leer_receta import leer_receta

# Main program loop
while True:
    print("\n" + "="*50)
    print("Bienvenido al recetario de 'Python'.")
    print("-"*50)
    mostrar_categorias()  # Show available categories
    print("\nEste es nuestro menú de opciones:")
    print("1. Ver recetas de una categoría")
    print("2. Agregar nueva receta a una categoría")
    print("3. Crear una categoria nueva")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")  
    print("-"*50)
    opcion = input("Seleccione una opción (1-6): ")  # User selects an option

    if opcion == "1":
        # View recipes in a category and read one
        print("\n" + "-"*40)
        categoria = input("Ingrese el nombre de la categoría: ")
        mostrar_recetas(categoria)  # Show recipes in the selected category
        print("\n¿Cuál receta desea ver?")
        nombre_receta = input("Ingrese el nombre de la receta: ")
        print("\nContenido de la receta:")
        print("-"*40)
        leer_receta(categoria, nombre_receta)  # Show recipe content
        print("\n" + "-"*40)

    elif opcion == "2":
        # Add a new recipe to a category
        print("\n" + "-"*40)
        categoria = input("Ingrese el nombre de la categoría: ")
        nombre_receta = input("Ingrese el nombre de la receta: ")
        print("Ingrese el contenido de la receta (escriba END en una línea nueva para finalizar):")
        lineas = []
        # Read multiline input until 'END' is entered
        while True:
            linea = input()
            if linea.strip() == "END":
                break
            lineas.append(linea)
        contenido = "\n".join(lineas)
        agregar_receta(categoria, nombre_receta, contenido)  # Save the new recipe
        print("\nReceta agregada exitosamente!\n" + "-"*40)

    elif opcion == "3":
        # Create a new category
        print("\n" + "-"*40)
        nombre_categoria = input("Ingrese el nombre de la nueva categoría: ")
        crear_categoria(nombre_categoria)
        print("\nCategoría creada exitosamente!\n" + "-"*40)

    elif opcion == "4":
        # Delete a recipe from a category
        print("\n" + "-"*40)
        categoria = input("Ingrese el nombre de la categoría: ")
        nombre_receta = input("Ingrese el nombre de la receta a eliminar: ")
        eliminar_receta(categoria, nombre_receta)
        print("\nReceta eliminada exitosamente!\n" + "-"*40)
    
    elif opcion == "5":
        # Delete a category and all its recipes
        print("\n" + "-"*40)
        nombre_categoria = input("Ingrese el nombre de la categoría a eliminar: ")
        eliminar_categoria(nombre_categoria)
        print("\nCategoría eliminada exitosamente!\n" + "-"*40)
    
    elif opcion == "6":
        # Exit the program
        print("\nGracias por usar el recetario. ¡Hasta luego!\n" + "="*50)
        break
    else:
        # Handle invalid option
        print("\nOpción no válida. Intente de nuevo.\n" + "-"*40)





