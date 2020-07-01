from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/bboleta')
def b_boleta():
    return render_template('menu_principal/busqueda_boleta.html')

@app.route('/bcliente')
def b_cliente():
    return render_template('menu_principal/busqueda_usuario.html')

@app.route('/dev-fallas')
def fallo():
    return render_template('menu_principal/ingreso_dev_falla.html')

@app.route('/ticket')
def ticket():
    return render_template('menu_principal/seguimiento_ticket.html')

@app.route('/informes')
def informes():
    return render_template('menu_principal/informes_general.html')

@app.route('/sugerencias')
def sug_rec():
    return render_template('menu_principal/sugerencias_reclamos.html')


if __name__ == '__main__':
    app.run(debug=True)