# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from presenca import Presenca


@app.route('/')
def index():
    presencas = Presenca.ler_presenca()

    menu = []
    menu.append({'active': True,
                'href': '/',
                'texto': 'Página principal'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})
    menu.append({'active': False,
                'href': '/anna',
                'texto': 'Sobre - Anna'})
    menu.append({'active': False,
                'href': '/andrea',
                'texto': 'Sobre - Andréa'})

    context = {'titulo': 'Página principal',
            'menu': menu,
            'presencas': presencas}

    return render_template('index.html', **context)

@app.route('/presenca')
def presenca():
    menu = []
    menu.append({'active': False,
                'href': '/',
                'texto': 'Página principal'})
    menu.append({'active': True,
                'href': '/presenca',
                'texto': 'Presença'})
    menu.append({'active': False,
                'href': '/anna',
                'texto': 'Sobre - Anna'})
    menu.append({'active': False,
                'href': '/andrea',
                'texto': 'Sobre - Andréa'})

    context = {'titulo': 'Marcar Presença',
            'menu': menu}

    return render_template('presenca.html', **context)


@app.route('/presenca/gravar', methods=['POST'])
def gravar():
    email_form = request.form['email']
    presenca_form = request.form['presenca']
    resposta_form = request.form['resposta']
    comentarios_form = request.form['comentarios']
    pres = Presenca(email_form, presenca_form, resposta_form, comentarios_form)
    pres.gravar_presenca()
    return redirect('/')

@app.route('/anna')
def anna():
    menu = []
    menu.append({'active': False,
                'href': '/',
                'texto': 'Página principal'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})
    menu.append({'active': True,
                'href': '/anna',
                'texto': 'Sobre - Anna'})
    menu.append({'active': False,
                'href': '/andrea',
                'texto': 'Sobre - Andréa'})

    context = {'titulo': 'Sobre - Anna',
            'menu': menu}

    return render_template('anna.html', **context)

@app.route('/andrea')
def andrea():
    menu = []
    menu.append({'active': False,
                'href': '/',
                'texto': 'Página principal'})
    menu.append({'active': False,
                'href': '/presenca',
                'texto': 'Presença'})
    menu.append({'active': False,
                'href': '/anna',
                'texto': 'Sobre - Anna'})
    menu.append({'active': True,
                'href': '/andrea',
                'texto': 'Sobre - Andréa'})

    context = {'titulo': 'Sobre - Andréa',
            'menu': menu}

    return render_template('andrea.html', **context)


app.run()
