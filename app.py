from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercise1', methods=['GET', 'POST'])
def exercise1():
    result = None
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
        result = {"promedio": promedio, "estado": estado}
    return render_template('exercise1.html', result=result)

@app.route('/exercise2', methods=['GET', 'POST'])
def exercise2():
    result = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        result = {"nombre_mas_largo": nombre_mas_largo, "longitud": len(nombre_mas_largo)}
    return render_template('exercise2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
