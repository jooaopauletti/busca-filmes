# 🎬 BuscaFlix

🔗 **Acesse a aplicação online:** https://buscaflix.onrender.com

Aplicação web em Python com Flask que consome a API do OMDb para buscar informações sobre filmes e séries: sinopse, ano, elenco, pôster e nota do IMDb.

## Funcionalidades
- 🔍 Busca por texto parcial, exibindo lista de resultados semelhantes (estilo Netflix)
- 🎞️ Página de detalhes com sinopse (traduzida automaticamente), ano, pôster e nota do IMDb
- 🖼️ Tratamento de pôster ausente ou indisponível
- ⚠️ Tratamento de título não encontrado
- ✅ Validação de campo vazio

## Como executar
1. Clone o repositório
2. Crie um ambiente virtual e ative-o
3. Instale as dependências
4. Crie um arquivo .env com sua chave da API OMDb

Comandos:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

No arquivo .env, adicione:
OMDB_API_KEY=sua_chave_aqui

5. Execute:
python app.py

6. Acesse no navegador: http://127.0.0.1:5000

## Tecnologias
- Python 3
- Flask
- Requests
- python-dotenv
- deep-translator
- API OMDb

## Autor
João Pauletti