# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:21:29 2022

@author: Carla Miquetan
"""


def cargar_canciones(billboard: str) -> dict:
    canciones = []

    with open(billboard, "r") as archivo:
        titulos = archivo.readline().split(",")
        print(titulos)
        campos = archivo.readline()
        while campos:
            campos = campos.split(",")
            cancion = {}
            cancion['posicion'] = campos[0]
            cancion['nombre_cancion'] = campos[1]
            cancion['nombre_artista'] = campos[2]
            cancion['anio'] = campos[3]
            cancion['letra'] = campos[4]
            campos = archivo.readline()
            canciones.append(cancion)

    return canciones


def buscar_cancion(canciones: list, nombre_cancion: str, anio: str) -> dict:
    elegida = None
    i = 0

    while i < len(canciones) and not elegida:
        cancion = canciones[i]
        if cancion["anio"] == anio and cancion["nombre_cancion"] == nombre_cancion:
            elegida = cancion
        i += 1

    return elegida


def canciones_anio(canciones: list, anio: int) -> list:
    lista_anio = []

    for cancion in canciones: 
        if cancion["anio"] == anio:
            cancion.pop("letra")
            lista_anio.append(cancion)
    return lista_anio   


def canciones_artista_periodo(canciones: list, artista: str, anio_inicio: int, anio_fin: int) -> list:
    resultado = []
    for cancion in canciones:

        if cancion['nombre_artista'] == artista and anio_inicio <= int(cancion['anio']) <= anio_fin:
            copia_cancion = {
               'posicion': cancion['posicion'],
               'nombre_cancion': cancion['nombre_cancion'],
               'nombre_artista': cancion['nombre_artista'],
               'anio': cancion['anio']
            }
            resultado.append(copia_cancion)
    return resultado


def todas_canciones_artista(canciones: list, artista: str) -> list:
    canciones_artistas = [cancion["nombre_cancion"] for cancion in canciones if cancion["nombre_artista"] == artista]
    return canciones_artistas


def todos_artistas_cancion(canciones: list, nombre_cancion: str) -> list:
    nombres_artistas = [cancion["nombre_artista"] for cancion in canciones if cancion["nombre_cancion"] == nombre_cancion]
    return nombres_artistas


def artistas_mas_populares(canciones: list, minimo: int) -> dict:
    dic = {}

    for cancion in canciones:
        if cancion["nombre_artista"] not in dic:
            dic[cancion["nombre_artista"]] = 1
        else:
            dic[cancion["nombre_artista"]] += 1

    canciones_minimo = {
        nombre_artista: surgimiento
        for nombre_artista, surgimiento in dic.items()
        if surgimiento > minimo
    }

    return canciones_minimo
          

def artista_estrella(canciones: list) -> dict:
    todos_los_artistas = artistas_mas_populares(canciones, 0)
    max_cantidad_de_apariciones = sorted(todos_los_artistas.values())[-1]
    for artista, surgimiento in todos_los_artistas.items():
        if surgimiento == max_cantidad_de_apariciones:
            return artista


def artistas_y_sus_canciones(canciones: list) -> dict:
    canciones_artistas = {}

    for cancion in canciones:
            encontrada = canciones_artistas.get(cancion["nombre_artista"], 0)
            if encontrada == 0:
                canciones_artistas[cancion["nombre_artista"]] = [cancion["nombre_cancion"]]
            else:
                if not cancion["nombre_cancion"] in canciones_artistas[cancion["nombre_artista"]]:
                    canciones_artistas[cancion["nombre_artista"]].append(cancion["nombre_cancion"])
                    
    return canciones_artistas


def canciones_y_art(canciones: list) -> dict:
    dic = {}

    for cancion in canciones:
        artista = cancion["nombre_cancion"]
        dic[artista] = dic.get(artista, 0)

    return dic


def promedio_canciones_por_artista(canciones) -> float:
    dic_artistas = artistas_y_sus_canciones(canciones)
    dic_canciones = canciones_y_art(canciones)

    if not dic_artistas:
        promedio = 0
    else:
        print("Longitud del diccionario canciones: %s" % len(dic_canciones))
        print("Longitud del diccionario artistas: %s" % len(dic_artistas))
        promedio = len(dic_canciones)/len(dic_artistas)

    return promedio