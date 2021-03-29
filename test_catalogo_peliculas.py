import os
from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas


opciones = None

while opciones != "5":
    try:
        opciones = str(input(
            "\n_____________BIENVENIDO_A_LA_SECCION_DE_PELICULAS______________\n\n"
            "Ingresa lo que quieres hacer: \n"
            "1) Agregar una Pelicula :)\n2) Ver la lista de Peliculas\n3) Eliminar la lista de Peliculas :(\n4) Crear nueva lista de peliculas\n5) Salir (Nooooo T.T)\nNota: Solo puedes escojer del 1 al 5, si escojes mal a proposito, tendras consecuencias =-=\n\nRespuesta: "
        ))
    except Exception as e:
        print("Escribe el numero correctamente", e)

    if opciones == "1":
        ag_pelicula = input("Ingresa el nombre de la pelicula: ")
        CatalogoPeliculas.agregar_pelicula(ag_pelicula)
        salir = input(
            "Pelicula agregada exitoxamente 7w7 (Presiona ENTER para seguir)")
    elif opciones == "2":
        print("\nAqui estan tus peliculas!!\n")
        CatalogoPeliculas.listar_peliculas()
        salir = input("Presiona ENTER para seguir")
    elif opciones == "3":
        CatalogoPeliculas.eliminar_pelicula()
        salir = input("Presiona ENTER para seguir")
    elif opciones == "4":
        CatalogoPeliculas.crear_archivo()
    elif opciones == "5":
        salir = input("\nBye :D (Presiona ENTER para salir)")
        os._exit(1)
