from flask import Flask, jsonify, send_from_directory
import sqlite3
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

def get_receitas():
    conn = sqlite3.connect('receitas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome, descricao, imagem_url FROM receitas")
    receitas = cursor.fetchall()
    conn.close()
    return [{"nome": r[0], "descricao": r[1], "imagem_url": r[2]} for r in receitas]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/receitas')
def receitas():
    return jsonify(get_receitas())

if __name__ == '__main__':
    app.run(debug=True)
