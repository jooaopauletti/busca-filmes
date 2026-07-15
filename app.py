from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('OMDB_API_KEY')

@app.route('/')
def index():
    titulo = request.args.get('titulo')
    filme = None

    if titulo:
        params = {
            "apikey": API_KEY,
            "t": titulo
        }
        resposta = requests.get("http://www.omdbapi.com/", params=params)
        filme = resposta.json()

    return render_template('index.html', filme=filme)

if __name__ == '__main__':
    app.run(debug=True)