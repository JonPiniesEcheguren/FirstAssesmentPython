from flask import Flask, request, render_template
from clases.PaisesCl import Espana
from clases.PaisesCl import Japon
from clases.PaisesCl import Mexico

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
