import sqlite3 as conector

caminhodb = "db\\geve.db"

def criarBanco():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cliente(
                                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT,
                                    telefone INTEGER,
                                    endereco TEXT)''')
    cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()

def adicionar_pessoas(nome,telefone,endereco):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    comando = '''INSERT INTO cliente (nome,telefone,endereco)
                      VALUES (:nome,:idade,:endereco);'''
    cursor.execute(comando, {
        "nome":nome,
        "idade":telefone,
        "endereco":endereco
    })
    conexao.commit()
    cursor.close()
    conexao.close()
    print("cliente cadastrado com sucesso")

def ver_pessoas():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM faculdade''')
    conexao.commit()
    for linha in cursor.fetchall():
        print(linha)
    cursor.close()
    conexao.close()
def atualizar_idade(nome, idade):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    comando = ('''UPDATE faculdade SET idade = ? WHERE nome = ?''',(idade,nome))
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Atualizado idade com sucesso")

def remove_pessoa(nome):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    comando = '''DELETE FROM faculdade WHERE nome=:nome'''
    cursor.execute(comando, {
        "nome":nome
    })
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Pessoa removida com sucesso")
