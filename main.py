from pathlib import Path
from modules.mostrar_categorias import mostrar_categorias
from modules.mostrar_recetas import mostrar_recetas
from modules.agregar_receta import agregar_receta
from modules.crear_categoria import crear_categoria
from modules.eliminar_receta import eliminar_receta
from modules.eliminar_categoria import eliminar_categoria
from modules.leer_receta import leer_receta

while True:
    print("Bienvenido al recetario de 'Python'.")
    mostrar_categorias()
    print("Estes es nuestro menu de opciones:")
    print("1. Ver recetas de una categoría")
    print("2. Agregar nueva receta a una categoría")
    print("3. Crear una categoria nueva")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")  
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        categoria = input("Ingrese el nombre de la categoría: ")
        mostrar_recetas(categoria)
        print("Cual receta desea ver?")
        nombre_receta = input("Ingrese el nombre de la receta: ")
        leer_receta(categoria, nombre_receta)

    elif opcion == "2":
        categoria = input("Ingrese el nombre de la categoría: ")
        nombre_receta = input("Ingrese el nombre de la receta: ")
        contenido = input("Ingrese el contenido de la receta: ")
        agregar_receta(categoria, nombre_receta, contenido)

    elif opcion == "3":
        nombre_categoria = input("Ingrese el nombre de la nueva categoría: ")
        crear_categoria(nombre_categoria)

    elif opcion == "4":
        categoria = input("Ingrese el nombre de la categoría: ")
        nombre_receta = input("Ingrese el nombre de la receta a eliminar: ")
        eliminar_receta(categoria, nombre_receta)
    
    elif opcion == "5":
        nombre_categoria = input("Ingrese el nombre de la categoría a eliminar: ")
        eliminar_categoria(nombre_categoria)
    
    elif opcion == "6":
        print("Gracias por usar el recetario. ¡Hasta luego!")
        break





