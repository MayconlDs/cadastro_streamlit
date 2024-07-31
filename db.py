import sqlite3

def cadastrar_usuario(nome, idade):
    # Criar a conexão e o cursor dentro da função
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    # Criar a tabela de usuários, se ainda não existir
    c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    ''')
    
    # Inserir o usuário na tabela
    c.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    
    # Salvar (commit) as alterações
    conn.commit()
    
    # Fechar a conexão
    conn.close()

def consultar_usuario(nome):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    resultado = c.fetchone()  # Usar fetchone para obter um único resultado
    
    conn.close()
    
    return resultado