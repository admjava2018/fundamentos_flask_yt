from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)