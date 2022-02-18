#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Billboard.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos

Carla
"""

import billboard as bb


def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """
    archivo = input(
        "Por favor ingrese la ruta al archivo CSV con las canciones: "
    )
    canciones = bb.cargar_canciones(archivo)
    if not canciones:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")
        
    return canciones


def ejecutar_buscar_cancion(canciones: list) -> None:
    """ Ejecuta la opción de buscar una canción dado el nombre y el año del 
    ranking al cual pertenece 
    """
    nombre_cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = input("Por favor ingrese el año de la canción que desea buscar: ")

    cancion = bb.buscar_cancion(canciones, nombre_cancion, anio)
    if cancion is None:
        print('No se encontró la canción')
    else:
        print(cancion)
        
    
def ejecutar_canciones_anio(canciones: list) -> None:
    """ Ejecuta la opción de consultar las canciones de un año dado """
    anio = input("Por favor ingrese el año que desea consultar: ")
    
    canciones_anio_ingresado = bb.canciones_anio(canciones, anio)
    
    if not canciones_anio_ingresado:
        print("No se encontraron canciones del año ", anio)
    else:
        print("Lista de canciones del año ", anio)
        for cancion in canciones_anio_ingresado:
            print()
            print("Posición de la canción : ", cancion["posicion"])
            print("Nombre de la canción: ", cancion["nombre_cancion"])
            print("Nombre del artista: ", cancion["nombre_artista"])
            print("Año: ", cancion["anio"])
            print()
    

def ejecutar_canciones_artista_periodo(canciones: list) -> None:
    """
    Ejecuta la opción de consultar las canciones de un artista dado en
    un periodo de tiempo definido 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inicio = int(input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))

    canciones_artista_periodo_ingresado = bb.canciones_artista_periodo(canciones, artista, anio_inicio, anio_fin)
    
    if not canciones_artista_periodo_ingresado:
        print(f"No se pudieron encontrar canciones del artista {artista} en el periodo {anio_inicio}-{anio_fin}")
    else:
        for canciones in canciones_artista_periodo_ingresado:
            print()
            print("Posición de la canción : ", canciones["posicion"])
            print("Nombre de la canción: ", canciones["nombre_cancion"])
            print("Nombre del artista: ", canciones["nombre_artista"])
            print("Año: ", canciones["anio"])
           

def ejecutar_todas_canciones_artista(canciones: list) -> None:
    """
    Ejecuta la opción de consultar todas las canciones de un artista dado
    """
    artista = input(
        "Por favor ingrese el nombre del artista que desea buscar: "
    )

    lista = bb.todas_canciones_artista(canciones, artista)
    print(f"Estas son todas las canciones de {artista} en el documento")
    print(lista)


def ejecutar_todos_artistas_cancion(canciones: list) -> None:
    """
    Ejecuta la opción de consultar todos los artistas que han interpretado
    una canción dada 
    """
    minimo = input("Por favor ingrese el nombre de la canción que desea buscar: ")

    lista = bb.todos_artistas_cancion(canciones, minimo)
    print(f"Estos son todos los artistas que han interpretado {minimo}")
    print(lista)


def ejecutar_artistas_mas_populares(canciones: list) -> None:
    """
    Ejecuta la opción de consultar los artistas más populares
    """
    minimo = int(input(
        "Por favor ingrese la cantidad mínima de canciones que desea buscar: ")
    )
    print(bb.artistas_mas_populares(canciones, minimo))


def ejecutar_artista_estrella(canciones: list) -> None:
    """
    Ejecuta la opción de consultar el artista estrella de todos los tiempos
    """
    print(bb.artista_estrella(canciones))


def ejecutar_artistas_y_sus_canciones(canciones: list) -> None:
    """
    Ejecuta la opción de consultar la lista completa de artistas del Billboard
    junto con sus canciones 
    """
    print(bb.artistas_y_sus_canciones(canciones))


def ejecutar_promedio_canciones_por_artista(canciones: list) -> None:
    """ Ejecuta la opción de consultar la cantidad promedio de canciones que los 
    artistas tienen en el listado de Billboard 
    """
    print(bb.promedio_canciones_por_artista(canciones))


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            canciones = ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 4:
            ejecutar_canciones_artista_periodo(canciones)
        elif opcion_seleccionada == 5:
            ejecutar_todas_canciones_artista(canciones)
        elif opcion_seleccionada == 6:
            ejecutar_todos_artistas_cancion(canciones)
        elif opcion_seleccionada == 7:
            ejecutar_artistas_mas_populares(canciones)
        elif opcion_seleccionada == 8:
            ejecutar_artista_estrella(canciones)
        elif opcion_seleccionada == 9:
            ejecutar_artistas_y_sus_canciones(canciones)
        elif opcion_seleccionada == 10:
            ejecutar_promedio_canciones_por_artista(canciones)
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()
