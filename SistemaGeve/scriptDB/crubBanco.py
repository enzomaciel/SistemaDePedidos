import sqlite3 as conector
caminhodb = "db\\geve.db"

#Criando banco e as tabelas do programa
def criarBanco():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario(
                                    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    username TEXT,
                                    password TEXT,
                                    email TEXT,
                                    aniversario DATA,
                                    cpf TEXT)''')
    
    cursor.fetchall()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cliente(
                                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT,
                                    telefone INTEGER,
                                    email TEXT)''')
    cursor.fetchall()
    cursor.execute('''CREATE TABLE IF NOT EXISTS produto(
                                    id_product INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name_product TEXT,
                                    unidade TEXT,
                                    valor REAL,
                                    comissao REAL)''')
    cursor.fetchall()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedido(
                                    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name_cliente TEXT,
                                    prazo TEXT,
                                    emissao DATA,
                                    subtotal REAL)''')
    cursor.fetchall()
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtopedido(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    num_pedido INTEGER,
                                    produto TEXT,
                                    emissao DATA,
                                    quantidade REAL,
                                    valor REAL,
                                    total REAL)''')
    
    cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()