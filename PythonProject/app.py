from flask import Flask, render_template, request

app = Flask(__name__)

# home
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # datos del formulari
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # aprobado o reprobado
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

# Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener los nombres del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Calcular el nombre con mas caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)

        return render_template('ejercicio2.html', nombre_largo=nombre_largo, longitud=longitud)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
