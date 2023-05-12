from abc import ABC, abstractmethod
from flask import Flask, request, render_template

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


app = Flask(__name__,template_folder='html')

@app.route("/")
def Paises():
    return render_template("start_Paises.html")

@app.route("/Paises", methods=['GET', 'POST'])
def mostrar_Paises():
    if request.method == 'POST':
        pais = request.form.get("Pais")
        capital = request.form.get("capital")
        idioma = request.form.get("idioma")
        region = request.form.get("region")
        moneda = request.form.get("moneda")
 # Obtener la Pais seleccionado por el usuario
        if pais == "México":
            Pais_ingresado = Mexico(pais, capital, idioma)
        elif pais == "Japón":
            Pais_ingresado = Japon(pais, capital, moneda)
        elif pais == "España":
            Pais_ingresado = Espana(pais, capital, region)
    # Insertar el código aquí
            
    # Renderizar la página de Paises con el Pais seleccionado
        return render_template("Paises.html", Pais=Pais_ingresado)

if __name__ == '__main__':
   app.run(debug=True)
