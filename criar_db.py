import sqlite3

conn = sqlite3.connect('receitas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS receitas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    imagem_url TEXT NOT NULL
)
''')

receitas = [
    ("Pão Francês", "Pão Francês crocante e fresco.", "https://th.bing.com/th/id/OIP.4jicxCGDy4jzp-EakOxBJwHaEc?rs=1&pid=ImgDetMain"),
    ("Pão de Centeio", "Pão de centeio integral, sabor rústico.", "https://th.bing.com/th/id/OIP.4jicxCGDy4jzp-EakOxBJwHaEc?rs=1&pid=ImgDetMain"),
    ("Pão de Forma", "Pão de forma macio e versátil.", "https://th.bing.com/th/id/OIP.4jicxCGDy4jzp-EakOxBJwHaEc?rs=1&pid=ImgDetMain"),
    ("Baguete", "Baguete clássica com crosta fina.", "https://th.bing.com/th/id/OIP.4jicxCGDy4jzp-EakOxBJwHaEc?rs=1&pid=ImgDetMain"),
    ("Pão Integral", "Pão integral saudável e nutritivo.", "https://th.bing.com/th/id/OIP.4jicxCGDy4jzp-EakOxBJwHaEc?rs=1&pid=ImgDetMain")
]

cursor.executemany('INSERT INTO receitas (nome, descricao, imagem_url) VALUES (?, ?, ?)', receitas)

conn.commit()
conn.close()

print("Banco receitas.db criado e populado com dados de exemplo.")
