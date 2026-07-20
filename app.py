from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('OMDB_API_KEY')

@app.route('/')
def index():
    titulo = request.args.get('titulo', '').strip()
    filme = None
    erro = None

    if titulo:
        params = {
            "apikey": API_KEY,
            "t": titulo
        }
        resposta = requests.get("http://www.omdbapi.com/", params=params)
        dados = resposta.json()

        if dados.get('Response') == 'True':
            filme = dados
        else:
            erro = dados.get('Error')

    return render_template('index.html', filme=filme, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)