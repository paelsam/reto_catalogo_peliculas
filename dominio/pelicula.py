class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f"{self.get_nombre()}\n"
