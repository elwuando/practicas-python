from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Hola, Arias. Flask está funcionando."


@app.route('/user/<nombre>')
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
































if __name__ == "__main__":
    app.run(debug=True)
