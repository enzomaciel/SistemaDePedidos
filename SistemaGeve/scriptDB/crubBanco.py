import sqlite3 as conector
caminhodb = "db\\geve.db"

#Criando banco e as tabelas do programa
def criarBanco():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
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
    conexao.commit()
    cursor.close()
    conexao.close()