import sqlite3 as conector

caminhodb = "db\\geve.db"

def cadastrarCliente(nome,telefone,email):
        conexao = conector.connect(caminhodb)
        cursor = conexao.cursor()
        comando = '''INSERT INTO cliente (nome,telefone,email)
                      VALUES (:nome,:idade,:email);'''
        cursor.execute(comando, {
            "nome":nome,
            "idade":telefone,
            "email":email
        })
        conexao.commit()
        cursor.close()
        conexao.close()
        print("cliente cadastrado com sucesso")

def ver_clientes():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM cliente''')
    conexao.commit()
    for linha in cursor.fetchall():
        print(linha)
    cursor.close()
    conexao.close()
def atualizar_idade(nome, idade):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    comando = ('''UPDATE cliente SET idade = ? WHERE nome = ?''',(idade,nome))
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Atualizado idade com sucesso")

def remove_cliente(nome):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    comando = '''DELETE FROM cliente WHERE nome=:nome'''
    cursor.execute(comando, {
        "nome":nome
    })
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Pessoa removida com sucesso")
