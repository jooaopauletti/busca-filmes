from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('OMDB_API_KEY')

@app.route('/')
def index():
    titulo = request.args.get('titulo', '').strip()
    resultados = None
    erro = None

    if titulo:
        params = {
            "apikey": API_KEY,
            "s": titulo
        }
        resposta = requests.get("http://www.omdbapi.com/", params=params)
        dados = resposta.json()

        if dados.get('Response') == 'True':
            resultados = dados['Search']
        else:
            erro = dados.get('Error')

    return render_template('index.html', resultados=resultados, erro=erro)

@app.route('/filme/<imdb_id>')
def detalhe(imdb_id):
    params = {
        "apikey": API_KEY,
        "i": imdb_id
    }
    resposta = requests.get("http://www.omdbapi.com/", params=params)
    dados = resposta.json()

    filme = None
    if dados.get('Response') == 'True':
        dados['Plot'] = GoogleTranslator(source='en', target='pt').translate(dados['Plot'])
        filme = dados

    return render_template('detalhe.html', filme=filme)

if __name__ == '__main__':
    app.run(debug=True)