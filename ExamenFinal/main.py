from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('inicio.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento, descuento=descuento)
    return render_template('ejercicio1.html', nombre=None, total_sin_descuento=None, total_con_descuento=None, descuento=None)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'juan' and contrasena == 'admin':
            mensaje = f"Bienvenido Administrador {usuario}"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

        return render_template('ejercicio2.html', mensaje=mensaje)
    return render_template('ejercicio2.html', mensaje=None)

if __name__ == '__main__':
    app.run(debug=True)
