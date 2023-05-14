import sqlite3 as conector

caminhodb = "SistemaGeve\\db\\clientes.db"

def criarBanco():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS faculdade(
                                    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT,
                                    idade INTEGER)''')
    cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()

def adicionar_pessoas(nome, idade):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    comando = '''INSERT INTO faculdade (nome,idade)
                      VALUES (:nome,:idade);'''
    cursor.execute(comando, {
        "nome":nome,
        "idade":idade
    })
    conexao.commit()
    cursor.close()
    conexao.close()
    print("pessoa cadastrada com sucesso")

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

def menu():
    print("===========Menu===========")
    print("1- adicionar pessoas")
    print("2- listar pessoas")
    print("3- atualizar a idade da Pessoa")
    print("4- excluir pessoa")
    print("0 - sair")

