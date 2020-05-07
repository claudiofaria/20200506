from aplicacao import app
from flask import render_template

@app.route('/')
def index():
    contexto = {'titulo': 'index.html',
            'mensagens': ['usuario1: olá', 'usuario2: olá'],
            'validar': 'valor'}
    return render_template('index.html', **contexto)

@app.route('/enviar')
def ennviar():
    contexto = {'titulo': 'Enviar Mensagem'}
    return render_template('mensagem.html', **contexto)

app.run(debug=True)