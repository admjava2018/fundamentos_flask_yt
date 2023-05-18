from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexión MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'database'

conexion = MySQL(app)

@app.before_request
def before_request():
    print("Antes de la petición...")

@app.after_request
def after_request(response):
    print("Después de la petición...")
    return response

@app.route('/')
def index():
    # return "<h1>Hello worldsss!</h1>"
    cursos = ['C++', 'Python', 'Java', 'Kotlin', 'C#', 'JavaScript']
    data = {
        'titulo': 'Index',
        'bienvenida': 'Hi everyone',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data = data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data = data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return 'Ok'

def pagina_no_encontrada(error):
    # return render_template('404.html')
    return redirect(url_for('index')) 

@app.route('/cursos')
def listar_cursos():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC"
        cursor.execute(sql)
        cursos = cursor.fetchall()
        print(cursos)
        data['cursos'] = cursos
        data['mensaje'] = "Éxito"
    except Exception as ex:
        data['mensaje'] = "Error: " + ex
    return jsonify(data)

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func = query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)