# Importa la clase datetime desde el módulo estándar datetime
from datetime import datetime
import re
import random
# Importa la clase Flask desde el modulo Flask.
from flask import Flask, render_template, request

# Crea la app Flask y __name__ le dice a Flask
# desde dónde se está ejecutando la app.
app = Flask(__name__)


# Le dice a Flask que asocie la URL raíz (/) con una función.
@app.route("/")
# Esta función devuelve una cadena de texto
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


@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    nombre = None
    celular = None

    if request.method == 'POST':

        nombre = request.form.get('nombre', None)
        celular = request.form.get('celular', None)

    return render_template('formulario.html', nombre=nombre, celular=celular)


@app.route('/limpiar', methods=['GET', 'POST'])
def limpiar_celular():
    numero = None
    mensaje = None

    if request.method == 'POST':
        numero = request.form.get('celular', None)
        mensaje = f'es valido'

        numero = re.sub(r'\D', '', str(numero))

        if numero.startswith('00'):
            numero = numero[2:]

        if numero.startswith('0'):
            numero = numero[1:]

        if numero.startswith('57'):
            numero = numero[2:]

        if len(numero) != 10:
            mensaje = f'no es valido'

        if not numero.startswith('3'):
            mensaje = f'no es valido'

    return render_template('formulario_num.html',
                           numero=numero, mensaje=mensaje)


@app.route('/contactos')
def contactos():
    clientes = [
        {"id": "cliente001", "nombre": "Andrea López",
         "telefono": "300-456-7890"},
        {"id": "cliente002", "nombre": "Carlos Pérez",
         "telefono": "(+57) 315 000 0000"},
        {"id": "cliente003", "nombre": "Mariana Díaz",
         "telefono": "31O-222-3344"},  # letra O en lugar de 0
        {"id": "cliente004", "nombre": "Luis Herrera",
         "telefono": "301@123@4567"},
        {"id": "cliente005", "nombre": "Sofía Gómez",
         "telefono": "12345"},
        {"id": "cliente006", "nombre": "Daniel Rodríguez",
         "telefono": "N/A"},
        {"id": "cliente007", "nombre": "Camila Torres",
         "telefono": "+57_300_999_1111"},
        {"id": "cliente008", "nombre": "Julián Ríos",
         "telefono": "300.123.4567"},
        {"id": "cliente009", "nombre": "Laura Martínez",
         "telefono": "Telefono no disponible"},
        {"id": "cliente010", "nombre": "Sebastián Cruz",
         "telefono": "00300-4455-667"},
        {"id": "cliente011", "nombre": "Valentina Ruiz",
         "telefono": "+57300ABC5678"},
        {"id": "cliente012", "nombre": "Mateo Ramírez",
         "telefono": "+57-@@@-####"},
        {"id": "cliente013", "nombre": "Isabella Moreno",
         "telefono": "+57 (315) 888-7777"},
        {"id": "cliente014", "nombre": "Tomás Vega",
         "telefono": "31 5555"},
        {"id": "cliente015", "nombre": "Luciana Castro",
         "telefono": "☎️ 3001234567"},
        {"id": "cliente016", "nombre": "Simón Méndez",
         "telefono": "300 123 456 789"},  # demasiado largo
        {"id": "cliente017", "nombre": "Gabriela León",
         "telefono": "+57-300-0000-0000"},
        {"id": "cliente018", "nombre": "Emilio Navarro",
         "telefono": "___"},
        {"id": "cliente019", "nombre": "Renata Flores",
         "telefono": "300-300-300"},
        {"id": "cliente020", "nombre": "Diego Cárdenas",
         "telefono": "null"},
        {"id": "cliente021", "nombre": "Natalia Romero",
         "telefono": "+57 300x999x888"},
        {"id": "cliente022", "nombre": "Juan Camilo",
         "telefono": "abc123"},
        {"id": "cliente023", "nombre": "Esteban Silva",
         "telefono": "😶"},
        {"id": "cliente024", "nombre": "Juliana Salas",
         "telefono": "+57 310-000-0000"},
        {"id": "cliente025", "nombre": "Felipe García",
         "telefono": " "},
        {"id": "cliente026", "nombre": "Diana Ortiz",
         "telefono": "+57 3a0 123 4567"},
        {"id": "cliente027", "nombre": "Camilo Páez",
         "telefono": "311\\444\\7777"},
        {"id": "cliente028", "nombre": "Manuela Rivas",
         "telefono": "+57-311-@@@-@@@@"},
        {"id": "cliente029", "nombre": "Ricardo Méndez",
         "telefono": "321-0000"},
        {"id": "cliente030", "nombre": "Paula Castaño",
         "telefono": "3109990000"}
    ]
    valido = request.args.get('limpiar', None)
    lista_valida = []
    if valido == 'True':
        for cliente in clientes:
            numero = cliente.get('telefono', None)
            numero = re.sub(r'\D', '', numero)

            if numero.startswith('00'):
                numero = numero[2:]

            if numero.startswith('0'):
                numero = numero[1:]

            if numero.startswith('57'):
                numero = numero[2:]

            if len(numero) == 10 and numero.startswith('3'):
                cliente['telefono'] = numero
                lista_valida.append(cliente)
        return render_template('contactos.html', clientes=lista_valida)

    return render_template('contactos.html', clientes=clientes)


'''reportes_almacen = [r for r in salida[almacen] if r.get('id') != id]'''
salida = {}


@app.route('/conta-clientes', methods=['GET', 'POST'])
def conta_clientes():
    # Extraemos el valor de accion y si no existe devuelve none
    accion = request.args.get('accion', None)
    # Validamos la accion Borrar
    if accion == 'borrar':
        # Lista vacia para guardar los reportes que no se eliminaran
        nuevo_reporte = []
        # obtenemos el ID del reporte que eliminaremos
        id = int(request.args.get('id', None))
        almacen = request.args.get('almacen', None)
        reportes_almacen = salida.get(almacen)

        for reporte in reportes_almacen:
            if reporte.get('id') != id:
                nuevo_reporte.append(reporte)
        # Nueva lista filtrada pero sin el ID que borramos
        salida[almacen] = nuevo_reporte

    if request.method == 'POST':
        fecha = request.form.get('fecha', None)
        clientes = int(request.form.get('clientes', None))
        facturas = int(request.form.get('facturas', None))
        valor = float(request.form.get('valor', None))
        almacen = request.form.get('almacen', None)

        reporte = {
            'id': random.randint(1000, 9999),
            'fecha': fecha,
            'clientes': clientes,
            'facturas': facturas,
            'valor_ventas': valor
        }

        if almacen not in salida:
            salida[almacen] = []

        salida[almacen].append(reporte)
    return render_template('formulario_cliente.html', datos=salida)


if __name__ == '__main__':
    app.run(debug=True)
