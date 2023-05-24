import sqlite3 as conector

caminhodb = "db\\geve.db"

def cadastrarProduto(nome,unidade,valor,comissao):
        conexao = conector.connect(caminhodb)
        cursor = conexao.cursor()
        comando = '''INSERT INTO produto (name_product,unidade,valor,comissao)
                      VALUES (:name_product,:unidade,:valor,:comissao);'''
        cursor.execute(comando, {
            "name_product":nome,
            "unidade":unidade,
            "valor":valor,
            "comissao":comissao
        })
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Produto cadastrado com sucesso")

def ver_produtos():
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

def remove_produto(nome):
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
