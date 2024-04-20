from flask import Flask, render_template, request, redirect, url_for, session, flash

class Console:
    def __init__(self, nome):
        self.nome=nome

console1 = Console('PlayStation')
console2 = Console('Xbox')
console3 = Console('PC')
console4 = Console('Mobile')

lista_consoles = [console1, console2, console3, console4]

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('League of Legends', 'MOBA', console3)
jogo2 = Jogo('Wild Rift', 'MOBA', console4)
jogo3 = Jogo('Valorant', 'FPS', console3)

lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos, consoles=lista_consoles)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo Jogo', consoles=lista_consoles)

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    nome_console = request.form['console']

    console = next((c for c in lista_consoles if c.nome == nome_console), None)
    if console:
        jogo = Jogo(nome, categoria, console)
        lista_jogos.append(jogo)
    else:
        print("Console não encontrado:", nome_console)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo='Faça seu Login')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'qwe123@' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        # flash(session['usuario_logado'] + ' logado com sucesso!')
        flash('Login realizado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')
    return redirect('/login')

app.run(debug=True)