import os


class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__())
            archivo.write("\n")
        except Exception as e:
            print("Ha ocurrido un error", e)
        finally:
            archivo.close()

    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catalogo de Peliculas:")
            print(archivo.read())
        except Exception as e:
            print("Ocurrio un error al listar peliculas: ", e)
        finally:
            archivo.close()

    @staticmethod
    def eliminar_pelicula():
        try:
            os.remove("peliculas.txt")
            print("Archivo", CatalogoPeliculas.ruta_archivo, "eliminado")
        except Exception as e:
            print("Ocurrio un error", e)

    @staticmethod
    def crear_archivo():
        CatalogoPeliculas.ruta_archivo = open("peliculas.txt", "w")
        salir = input(
            f"Archivo creado.")
