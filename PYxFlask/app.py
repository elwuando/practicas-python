# Importa la clase datetime desde el módulo estándar datetime
from datetime import datetime
# Importa la clase Flask desde el modulo Flask.
from flask import Flask, render_template, request

# Crea la app Flask y __name__ le dice a Flask desde dónde se está ejecutando la app.
app = Flask(__name__)

# Le dice a Flask que asocie la URL raíz (/) con una función.
@app.route("/")
# Esta función devuelve una cadena de texto
def inicio():
    return "Hola, Arias. Flask está funcionando."

# Define una ruta dinámica.
@app.route('/user/<nombre>')
# Define una función que recibe el valor capturado en la URL.
def usuario(nombre):
    return f'Usuario: {nombre}'


@app.route('/sumatoria')
def suma():
    a = 3
    b = 2
    resultado = a + b
    return str(resultado)


@app.route('/saludo/<nombre>')
def saludar(nombre):
    hora = datetime.now().hour
    print(hora)
    if hora >= 6 and hora < 12:
        saludo = 'buen dia Dios esta de tu lado'
    elif hora >= 12 and hora < 19:
        saludo = 'buenas tardes Dios esta de tu lado'
    else:
        saludo = 'buenas noches Dios esta de tu lado'

    return f'{saludo}, {nombre}'


@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    nombre = None
    celular = None
    if request.method == 'POST':
        print(request.form)
        nombre = request.form.get('nombre', None)
        celular = request.form.get('celular', None)   
    print(nombre, celular)
    
    return render_template('formulario.html', persona=nombre, numero=celular)


if __name__ == "__main__":
    app.run(debug=True)
