# Importa tus módulos aquí
from data.biblioteca import libros, categorias
from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    contar_libros,
    promedio_paginas,
    agregar_categoria
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Llama a mostrar_disponibles()
        mostrar_disponibles(libros)
        
    elif opcion == "2":
        buscar_por_paginas(libros,400)

        # Llama a buscar_por_paginas()
        
    elif opcion == "3":
        print ("total libros:",
               contar_libros(libros))
        # Llama contar_libros()
        # Llama promedio_paginas()
        
    # ... completa las demás opciones
    elif opcion=="4":
        nueva=input("nueva categoria: ")
        agregar_categoria(categorias,nueva)
    elif opcion=="5":    
        continuar = "n"