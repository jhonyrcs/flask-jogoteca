from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('League of Legends', 'MOBA', 'PC')
    jogo2 = Jogo('Wild Rift', 'MOBA', 'Mobile')
    jogo3 = Jogo('Valorant', 'FPS', 'PC')

    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

app.run()