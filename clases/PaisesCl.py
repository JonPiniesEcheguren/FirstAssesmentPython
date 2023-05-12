from abc import ABC, abstractmethod

class Pais(ABC):
    def __init__(self, nombre, capital):
        self.nombre = nombre
        self.capital = capital

    @abstractmethod
    def descripcion(self):
        pass

class Mexico(Pais):
    def __init__(self, nombre, capital, idioma):
        super().__init__(nombre, capital)
        self.idioma = idioma

    def descripcion(self):
        return(f"México es un país de América del Norte, cuya capital es {self.capital} y su idioma oficial es el {self.idioma}.")

class Japon(Pais):
    def __init__(self, nombre, capital, moneda):
        super().__init__(nombre, capital)
        self.moneda = moneda

    def descripcion(self):
        return(f"Japón es un país de Asia, cuya capital es {self.capital} y su moneda oficial es el {self.moneda}.")
    
class Espana(Pais):
    def __init__(self, nombre, capital, region):
        super().__init__(nombre, capital)
        self.region = region

    def descripcion(self):
        return(f"España es un país de Europa, cuya capital es {self.capital} y se encuentra en la región de {self.region}.")